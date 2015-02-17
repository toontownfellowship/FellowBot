import willie.module
from willie.modules.getmods import *

@willie.module.commands('quit')
def quit(bot, trigger):
    if any(s == trigger.nick for s in mods):
        bot.write(['quit', trigger.group(2)])
