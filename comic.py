import willie
import subprocess
import os
import yaml
import re
import random
from PIL import Image

@willie.module.commands('comic')
def comic(bot, trigger):
    stored_lines = len(bot.memory['log'][trigger.sender]['lines'])
    offset_length = stored_lines - random.randint(7,12)
    try:
        if trigger.bytes.split(' ', 1)[1].isdigit():
            length = int(trigger.bytes.split(' ', 1)[1])
            offset_length = stored_lines - length
    except:
        pass
    f = open('/home/svchost/spittoon/spec', 'w')
    if not len(bot.memory['log'][trigger.sender]['lines']) < 11:
        for x in range(offset_length, len(bot.memory['log'][trigger.sender]['lines'])):
            line = ''
            if bot.memory['log'][trigger.sender][u'lines'][x][:6] == 'ACTION':
                line = bot.memory['log'][trigger.sender]['nicks'][x] + '* ' + bot.memory['log'][trigger.sender]['nicks'][x] + bot.memory['log'][trigger.sender][u'lines'][x][6:] + '\n'
            else:
                line = '' + bot.memory['log'][trigger.sender]['nicks'][x] + ': ' + bot.memory['log'][trigger.sender][u'lines'][x] + '\n'
            f.write(line)
    else:
        for x in range(0, len(bot.memory['log'][trigger.sender]['lines'])):
            f.write(bot.memory['log'][trigger.sender]['nicks'][x] + ': ' + bot.memory['log'][trigger.sender][u'lines'][x] + '\n')
    f.close()
    subprocess.call(['/home/svchost/spittoon/comic.sh'])
    subprocess.call(['/home/svchost/spittoon/imgur.sh'])
    f = open('/home/svchost/spittoon/url', 'r')
    bot.say('Here is your comic: ' + f.read())
    f.close()
    os.remove('/home/svchost/spittoon/url')

@willie.module.commands('comicimg')
def comicimg(bot, trigger):
    nick = trigger.nick
    avatar_url = trigger.bytes.split(' ')[1]
    avatar_base_name = avatar_url.rsplit('/',1)[1]
    subprocess.call(['wget', avatar_url])
    im = Image.open(avatar_base_name)
    im.save(avatar_base_name.rsplit('.',1)[0] + '.png')
    avatar_base_name = avatar_base_name.rsplit('.',1)[0] + '.png'
    subprocess.call(['mv', avatar_base_name, 'spittoon/examples/artwork/poses/' + trigger.nick + '-standing1.png'])
    subprocess.call(['cp', 'spittoon/examples/artwork/faces/svchost-happy.png', 'spittoon/examples/artwork/faces/' + trigger.nick + '-happy.png'])
    with open ('spittoon/examples/config.yaml', 'r') as myfile:
        data=myfile.read()
    config = yaml.load(data)
    if str(nick) not in config['characters']:
        config['characters'].append(str(nick))
    stream = file('spittoon/examples/config.yaml', 'w')
    config = yaml.dump(config, stream)
    bot.say('Saved ' + avatar_base_name + '!')
    
@willie.module.rule('\A.*\Z')
def remember(bot, trigger):
    data = re.sub(r'[\x01-\x1f]','',trigger.bytes)
    data = data.encode('ascii', 'ignore')
    if data[:1] == '.' or data[:1] == '!' or data[:1] == '`':
        return
    if not bot.memory.contains('log'):
        bot.memory['log'] = {}	
    if not trigger.sender in bot.memory['log']:
        bot.memory['log'][trigger.sender] = {}
        bot.memory['log'][trigger.sender]['lines'] = [data]
        bot.memory['log'][trigger.sender]['nicks'] = [trigger.nick]
    else:
        bot.memory['log'][trigger.sender]['lines'].append(data)
        bot.memory['log'][trigger.sender]['nicks'].append(trigger.nick)
    if len(bot.memory['log'][trigger.sender]['lines']) >= 201:
        length = len(bot.memory['log'][trigger.sender]['lines'])
        length -= 1
        for x in range(0, length):
            del bot.memory['log'][trigger.sender]['lines'][0]
            del bot.memory['log'][trigger.sender]['nicks'][0]
