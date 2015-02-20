from willie.module import *

@require_privilege(OP)
@commands('news')
def news(bot, trigger):
    if not trigger.group(2):
        bot.msg(trigger.nick, 'Syntax: .news (news)')
    else:
        bot.msg('The_Judge', 'TOPIC #toontownfellowship ' + trigger.group(2))
