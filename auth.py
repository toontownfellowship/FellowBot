import willie.module

@willie.module.commands('auth')
@willie.module.rate(18000) # 5 hour cooldown
def auth(bot, trigger):
    """
NEVER EVER commmit this password to git
    """
    bot.write(['authserv auth fellowshipbot password'])
