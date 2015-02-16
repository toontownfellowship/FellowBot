import willie.module
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
@willie.module.rate(60) #1 minute cooldown for one user
def gt(bot, trigger):
    operator = '#TTFSInvasions' #this can also be a '#channel'
    words = trigger.group(2).split(' ')
    if words[0] == 'request':
        if len(words) >= 2:
            if len(words) == 3:
                cogs2 = ['pencil pusher', 'head hunter', 'corporate raider',
                         'big cheese', 'bottom feeder', 'double talker',
                         'ambulance chaser', 'back stabber', 'spin doctor',
                         'leagal eagle', 'big wig', 'short change', 'penny pincher',
                         'bean counter', 'number cruncher', 'money bags', 'loan shark',
                         'robber baron', 'cold caller', 'name dropper', 'glad hander',
                         'mover shaker', 'two face', 'mr. hollywood']
                cogname = words[1] + ' ' + words[2]
                if any(b == cogname for b in cogs2):
                    bot.reply('Your request has been submitted.')
                    bot.msg(operator, trigger.nick + ' has requested an invasion of ' + words[1] + ' ' + words[2])
                else:
                    bot.msg(trigger.nick, 'Please use the correct name for the cog, try again in one minute. a list can be found http://pastebin.com/3FxNti9T')
            else:
                cogs1 = ['flunky', 'yesman', 'micromanager', 'downsizer',
                         'bloodsucker', 'tightwad', 'telemarketer', 'mingler']
                if any(a == words[1] for a in cogs1):
                    bot.reply('Your request has been submitted.')
                    bot.msg(operator, trigger.nick + ' has requested an invasion of ' + words[1])
                else:
                    bot.msg(trigger.nick, 'Please use the correct name for the cog, try again in one minute. a list can be found http://pastebin.com/3FxNti9T')
        else:
            bot.msg(trigger.nick, 'Please include a cog name!')


@willie.module.commands('auth')
@willie.module.rate(18000) # 5 hour cooldown
def auth(bot, trigger):
    bot.write(['authserv auth fellowshipbot password'])


@willie.module.commands('help')
def help(bot, trigger):
    bot.msg(trigger.nick, "Here's the commands for FellowshipBot! http://pastebin.com/8rQpVzdC")

@willie.module.require_privilege(OP)
@willie.module.commands('rules')
def rules(bot, trigger):
    bot.msg('chanserv', trigger.sender + ' KICK ' + trigger.group(2) + ' Please read the rules again before re-joining -> https://privatepaste.com/0bbd0fed32')
                   
    
    
