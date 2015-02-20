
from willie.module import *

@require_privilege(OP)
@commands('rules')
def rules(bot, trigger):
    if not trigger.group(2):
        bot.msg(trigger.nick, 'Please add a name to the command')
    else:
        bot.msg('Chanserv', trigger.sender + ' KICK ' + trigger.group(2) + ' Please read the rules again before re-joining -> https://www.toontownfellowship.com/irc/')
