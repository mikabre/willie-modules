import sys
sys.path.append('/home/svchost/madlibs')
import willie
import shelve
import madlibs
from datetime import datetime, timedelta

@willie.module.commands('yiff')
def yiff(bot, trigger):
    now = datetime.now()
    time = 'time'
    if not time in bot.memory:
        bot.memory[time] = now - timedelta (seconds = 1000)
    if (now - bot.memory[time]) < timedelta (seconds = 60):
        return
    ML = madlibs.Madlibs('/home/svchost/madlibs/yiffy.json')
    story = ML.story()
    try:
        target = trigger.bytes.split(' ')[1]
    except:
        target = trigger.nick
    yiffer = trigger.nick
    story = story.replace("$1", yiffer)
    story = story.replace("$2", target)
    bot.action(story)
    bot.memory[time] = datetime.now()
