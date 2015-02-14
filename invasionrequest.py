import willie.module
authservuser = 'user'
authservpass = 'pass'
"""
--------------------
|LOGGING IN THE BOT|
--------------------
replace above variables with credentials, then say anywhere to the bot (private message, etc) ".auth"
MAKE SURE YOUR NICKNAME IS INCLUDED IN AN IF STATEMENT FOR THIS TO WORK FOR YOU
----------
|COMMANDS|
----------
making a command based off of the fellowship command-
make an else if statement that checks the words[0] to be the command
-
    elif words[0] == 'yo':
        print 'k'
-
".fellowshipbot yo" will print k

"""
@willie.module.commands('fellowshipbot')
@willie.module.rate(300) #5 minute cooldown for one user
def gt(bot, trigger):
    operator = '#testingland' #this can also be a '#channel'
    words = trigger.group(2).split(' ')
    if words[0] == 'request':
        if len(words) >= 2:
            if len(words) == 3:
                bot.reply('Your request has been submitted.')
                bot.msg(operator, trigger.nick + ' has requested an invasion of ' + words[1] + ' ' + words[2])
            else:
                bot.reply('Your request has been submitted.')
                bot.msg(operator, trigger.nick + ' has requested an invasion of ' + words[1])
        else:
            bot.msg(trigger.nick, 'Please include a cog name!')


@willie.module.commands('auth')
def auth(bot, trigger):
    if trigger.nick == 'Captain':
        bot.msg('authserv', authservuser + ' ' + authservpass)
    if trigger.nick == 'The_Judge':
        bot.msg('authserv', authservuser + ' ' + authservpass)
