import willie

@willie.module.commands('motd')
def motd(bot, trigger):
    bot.say("Updated as of November 19th, 2013: '.dunno'")
