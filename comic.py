import willie
import subprocess
import os
import yaml
import Image

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
    nick = trigger.nick
    avatar_url = trigger.bytes.split(' ')[1]
    avatar_base_name = avatar_url.rsplit('/',1)[1]
    subprocess.call(['wget', avatar_url])
    im = Image.open(avatar_base_name)
    im.save(avatar_base_name.rsplit('.',1)[0] + '.png')
    avatar_base_name = avatar_base_name.rsplit('.',1)[0] + '.png'
    subprocess.call(['mv', avatar_base_name, 'statico-spittoon/examples/artwork/poses/' + trigger.nick + '-standing1.png'])
    subprocess.call(['cp', 'statico-spittoon/examples/artwork/faces/svchost-happy.png', 'statico-spittoon/examples/artwork/faces/' + trigger.nick + '-happy.png'])
    with open ('statico-spittoon/examples/config.yaml', 'r') as myfile:
        data=myfile.read()
    config = yaml.load(data)
    if str(nick) not in config['characters']:
        config['characters'].append(str(nick))
    stream = file('statico-spittoon/examples/config.yaml', 'w')
    config = yaml.dump(config, stream)
    bot.say('Saved ' + avatar_base_name + '!')
    
@willie.module.rule('\A\w.*\Z')
def remember(bot, trigger):
    data = ''.join([i if ord(i) < 128 else '' for i in trigger.bytes])
    if not bot.memory.contains('log'):
        bot.memory['log'] = {}	
    if not trigger.sender in bot.memory['log']:
        bot.memory['log'][trigger.sender] = {}
        bot.memory['log'][trigger.sender]['lines'] = [data]
        bot.memory['log'][trigger.sender]['nicks'] = [trigger.nick]
    else:
        bot.memory['log'][trigger.sender]['lines'].append(data)
        bot.memory['log'][trigger.sender]['nicks'].append(trigger.nick)
    if len(bot.memory['log'][trigger.sender]['lines']) >= 21:
        length = len(bot.memory['log'][trigger.sender]['lines'])
        length -= 20
        for x in range(0, length):
            del bot.memory['log'][trigger.sender]['lines'][0]
            del bot.memory['log'][trigger.sender]['nicks'][0]
