# -*- coding: utf-8 -*-
import willie
import random

@willie.module.commands('dunno')
def dunno(bot, trigger):
    x = random.randint(0,2)
    dunno = [u"‾\(ツ)/‾", u"¯\(º_o)/¯", u"¯\_(シ)_/¯"]
    bot.say(dunno[x])

@willie.module.commands('downy')
def downy(bot, trigger):
    bot.say(".'\x1f/\x1f)")


@willie.module.commands('lv')
def lv(bot, trigger):
    bot.say(u"♥")

@willie.module.commands('id')
def id(bot, trigger):
    x = random.randint(0,4)
    y = random.randint(0,999)

    if y == 999:
        dbladez = ['\x03\x02illegal dbladez\x02','\x03\x02I snuck dbladez into prison up my ass.\x02','\x03\x02I love sniffing whole lines of dbladez.\x02','\x03\x02Twenty-five years in prison was worth it for just one hit of dbladez\x02','\x03\x02Taking dbladez ruined my life.\x02']
        bot.say(dbladez[x])
    else:
        bot.say("\x03\x02illegal drugs\x02")

@willie.module.commands('ld')
def ld(bot, trigger):
    x = random.randint(0,29)
    if x == 9:
        bot.say("\x03\x02There are no legal drugs.\x02")
    elif x == 19:
        bot.say("\x03\x02All drugs are illegal.\x02")
    elif x == 29:
        bot.say("\x03\x02Your drug use has been logged and reported.\x02")
    else:
        bot.say("\x03\x02legal drugs\x02")

@willie.module.rule('xD')
def xD(bot, trigger):
    x = random.randint(0,4)
    y = random.randint(0,99)
    if y == 99:
        bot.say('hi every1 im new!!!!!!! holds up spork my name is katy but u can call me t3h PeNgU1N oF d00m!!!!!!!! lol…as u can see im very random!!!! thats why i came here, 2 meet random ppl like me _… im 13 years old (im mature 4 my age tho!!) i like 2 watch invader zim w/ my girlfreind (im bi if u dont like it deal w/it) its our favorite tv show!!! bcuz its SOOOO random!!!! shes random 2 of course but i want 2 meet more random ppl =) like they say the more the merrier!!!! lol…neways i hope 2 make alot of freinds here so give me lots of commentses!!!! DOOOOOMMMM!!!!!!!!!!!!!!!! <--- me bein random again _^ hehe…toodles!!!!!')
        bot.say('loves and waffles,')
        bot.say('t3h PeNgU1N oF d00m')
    else:
        if y < 49:
            xd = ['xd', 'xD', 'XD', 'xDD', 'XDD']
            bot.say(xd[x])
