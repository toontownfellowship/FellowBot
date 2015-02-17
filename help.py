import willie.module
@willie.module.commands('help')
def help(bot, trigger):
    trigger.sender = trigger.nick
    bot.reply("Here's the commands for FellowshipBot! http://pastebin.com/8rQpVzdC", notice=True)
