import willie

@willie.module.commands('tell')
def tell(bot, trigger):
    try:
        name = trigger.bytes.split(' ')[1].lower()
    except:
        bot.say("You didn't give me a name!")
        return
    try:
        message = trigger.bytes.split(' ', 2)[2]
    except:
        bot.say("You didn't give me a message to leave " + name + ".")
        return
    large_message = trigger.nick + ' left a message for you: ' + message
    if not bot.memory.contains('tell'):
        bot.memory['tell'] = {}
    if not name in bot.memory['tell']:
        bot.memory['tell'][name] = [large_message]
    else:
        bot.memory['tell'][name].append(large_message)
    bot.say('Okay!')

@willie.module.rule('.*')
def remember(bot, trigger):
    if not 'tell' in bot.memory:
        bot.memory['tell'] = {}
    if trigger.nick in bot.memory['tell']:
        output = bot.memory['tell'][trigger.nick]
        bot.memory['tell'].pop(trigger.nick)
        for message in output:
            bot.say('Hi, ' + trigger.nick + '! ' + message)
