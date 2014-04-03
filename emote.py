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
