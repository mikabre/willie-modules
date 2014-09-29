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
    bot.say("\x03\x02illegal drugs\x02")

@willie.module.commands('ld')
def ld(bot, trigger):
    bot.say("\x03\x02legal drugs\x02")
