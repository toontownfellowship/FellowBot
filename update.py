from willie.module import *

@require_privilege(OP)
@commands('Update')
def reload_mods(bot, trigger):
    bot.reply('Fellowshipbot has been Updated!')
    bot.setup() #reloads modules
