import willie.module
@willie.module.commands('help')
def help(bot, trigger):
    bot.msg(trigger.nick, "The commands for Fellowshipbot are located in the guide here -> https://www.toontownfellowship.com/irc/")
