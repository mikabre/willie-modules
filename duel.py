import willie
import random
import sqlite3 as lite
import sys
import re
from datetime import datetime, timedelta

@willie.module.commands('duel')
def duel(bot, trigger):
    x = random.randint(0,1)
    nick = trigger.nick.lower()
    con = lite.connect('fiolina.db')
    #if pattern.search(nick):
    #    bot.say("Your name sucks, take out any special characters. Underscores are okay.")
    #    return
    #pattern=re.compile("\\\\")
    #if pattern.search(nick):
    #    bot.say("Your name sucks, take out any special characters. Underscores are okay.")
    #    return
    try:
        target = trigger.bytes.split(' ')[1].lower()
        #pattern=re.compile("\W|\\\\")
        #if pattern.search(target):
        #    bot.say("Your target's name sucks, take out any special characters. Underscores are okay.")
        #    return
        target_upper = trigger.bytes.split(' ')[1]
    except:
        target = "fiolina"
        target_upper = "me"
    if nick == target:
        bot.say("You can't duel yourself!")
        return
    channel = trigger.sender
    with con:
        cur = con.cursor()
        cur.execute("SELECT player_one, player_two FROM duel WHERE (player_one = ? and player_two = ? ) or (player_one = ? and player_two = ?)", (nick,target,target,nick,))
        data = cur.fetchone()
        if data == None:
            if nick < target:
                cur.execute("INSERT INTO duel (player_one, player_two, wins_one, wins_two) VALUES(? , ?, 0, 0)", (nick,target,))
            else:
                cur.execute("INSERT INTO duel (player_one, player_two, wins_one, wins_two) VALUES(? , ?, 0, 0)", (target,nick,))
        cur.execute("SELECT player_one, player_two FROM duel WHERE (player_one = ? and player_two = ? ) or (player_one = ? and player_two = ?)", (nick,target,target,nick,))
        data = cur.fetchone()
        player_one = ""
        if nick == data[0]:
            player_one = nick
        else:
            player_one = target
        cur.execute("SELECT id FROM duel WHERE (player_one = ? and player_two = ? ) or (player_one = ? and player_two = ?)", (nick,target,target,nick,))
        data = cur.fetchone()
        duel_id = data[0]
        now = datetime.now()
        if not trigger.nick in bot.memory:
            bot.memory[trigger.nick] = now - timedelta (seconds = 1000) 
        if channel != "#testing":
            if (now - bot.memory[trigger.nick]) < timedelta (seconds = 300):
                bot.say('Please wait five minutes before dueling again.')
                return
        if x == 0 and player_one == nick:
            cur.execute("UPDATE duel SET wins_one = wins_one + 1 where id = ? ",(duel_id,))
        elif x == 0 and player_one == target:
            cur.execute("UPDATE duel SET wins_two = wins_two + 1 where id = ? ",(duel_id,))
        elif x == 1 and player_one == nick:
            cur.execute("UPDATE duel SET wins_two = wins_two + 1 where id = ? ",(duel_id,))
        elif x == 1 and player_one == target:
            cur.execute("UPDATE duel SET wins_one = wins_one + 1 where id = ? ",(duel_id,))
        else:
            bot.say("svchost is a really shitty programmer and somehow missed this bug.")
        cur.execute("SELECT wins_one, wins_two FROM duel WHERE (player_one = ? and player_two = ? ) or (player_one = ? and player_two = ?)", (nick,target,target,nick,))
        data = cur.fetchone()
        if x == 0 and player_one == nick:
            bot.say("%s has defeated %s in honorable combat, and %s's record against %s stands at %s wins and %s losses." % (trigger.nick, target_upper, trigger.nick, target_upper, data[0], data[1]))
            bot.memory[trigger.nick] = datetime.now() 
        elif x == 0 and player_one == target:
            bot.say("%s has defeated %s in honorable combat, and %s's record against %s stands at %s wins and %s losses." % (trigger.nick, target_upper, trigger.nick, target_upper, data[1], data[0]))
            bot.memory[trigger.nick] = datetime.now()
        elif x == 1 and player_one == nick:
            bot.say("%s has been defeated by %s in honorable combat, and %s's record against %s stands at %s wins and %s losses." % (trigger.nick, target_upper, trigger.nick, target_upper, data[0], data[1]))
            bot.memory[trigger.nick] = datetime.now()
        elif x == 1 and player_one == target:
            bot.say("%s has been defeated by %s in honorable combat, and %s's record against %s stands at %s wins and %s losses." % (trigger.nick, target_upper, trigger.nick, target_upper, data[1], data[0]))
            bot.memory[trigger.nick] = datetime.now()
