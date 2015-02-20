from willie.module import *

@require_privilege(VOICE) #voice or OP will work
@commands('Update')
def reload_mods(bot, trigger):
    bot.reply('Fellowshipbot has been Updated!')
    bot.setup() #reloads modules
