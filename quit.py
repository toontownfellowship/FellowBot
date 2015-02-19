from willie.module import *

@require_privilege(OP)
@commands('quit')
def quit(bot, trigger):
    bot.write(['notice', trigger.sender, trigger.group(2)])
