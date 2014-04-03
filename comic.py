import willie
import subprocess
import os

@willie.module.commands('comic')
def comic(bot, trigger):
    f = open('/home/svchost/statico-spittoon/spec', 'w')
    if not len(bot.memory['log'][trigger.sender]['lines']) < 11:
        for x in range(12, len(bot.memory['log'][trigger.sender]['lines'])):
            f.write(bot.memory['log'][trigger.sender]['nicks'][x] + ': ' + bot.memory['log'][trigger.sender]['lines'][x] + '\n')
    else:
        for x in range(0, len(bot.memory['log'][trigger.sender]['lines'])):
            f.write(bot.memory['log'][trigger.sender]['nicks'][x] + ': ' + bot.memory['log'][trigger.sender]['lines'][x] + '\n')
    f.close()
    subprocess.call(['/home/svchost/statico-spittoon/comic.sh'])
    subprocess.call(['/home/svchost/statico-spittoon/imgur.sh'])
    f = open('/home/svchost/statico-spittoon/url', 'r')
    bot.say('Here is your comic: ' + f.read())
    f.close()
    os.remove('/home/svchost/statico-spittoon/url')

@willie.module.commands('comicimg')
def comicimg(bot, trigger):
    avatar_url = trigger.bytes.split(' ')[1]
    avatar_base_name = avatar.rsplit('/',1)[0]
    subprocess.call(['wget', avatar, '&&', 'mv', avatar_base_name, 'examples/artwork/poses/' + trigger.sender + ''])

@willie.module.rule('\A\w.*\Z')
def remember(bot, trigger):
    if not bot.memory.contains('log'):
        bot.memory['log'] = {}	
    if not trigger.sender in bot.memory['log']:
        bot.memory['log'][trigger.sender] = {}
        bot.memory['log'][trigger.sender]['lines'] = [trigger.bytes]
        bot.memory['log'][trigger.sender]['nicks'] = [trigger.nick]
    else:
        bot.memory['log'][trigger.sender]['lines'].append(trigger.bytes)
        bot.memory['log'][trigger.sender]['nicks'].append(trigger.nick)
    if len(bot.memory['log'][trigger.sender]['lines']) >= 21:
        length = len(bot.memory['log'][trigger.sender]['lines'])
        length -= 20
        for x in range(0, length):
            del bot.memory['log'][trigger.sender]['lines'][0]
            del bot.memory['log'][trigger.sender]['nicks'][0]
