import willie.module

@willie.module.commands('request')
@willie.module.rate(60) #1 minute cooldown for one user
def gt(bot, trigger):
    operator = '#TTFSInvasions' #this can also be a '#channel'
    words = trigger.group(2).split(' ')
    if len(words) >= 1:
        if len(words) == 2:
            cogs2 = ['pencil pusher', 'head hunter', 'corporate raider',
                'big cheese', 'bottom feeder', 'double talker',
                'ambulance chaser', 'back stabber', 'spin doctor',
                'leagal eagle', 'big wig', 'short change', 'penny pincher',
                'bean counter', 'number cruncher', 'money bags', 'loan shark',
                'robber baron', 'cold caller', 'name dropper', 'glad hander',
                'mover shaker', 'two face', 'mr. hollywood']
            cogname = words[0] + ' ' + words[1]
            if any(b == cogname for b in cogs2):
                bot.reply('Your request has been submitted.')
                bot.msg(operator, trigger.nick + ' has requested an invasion of ' + words[0] + ' ' + words[1])
            else:
                bot.msg(trigger.nick, 'Please use the correct name for the cog, try again in one minute. a list can be found http://pastebin.com/3FxNti9T')
        else:
            cogs1 = ['flunky', 'yesman', 'micromanager', 'downsizer',
                    'bloodsucker', 'tightwad', 'telemarketer', 'mingler']
            if any(a == words[0] for a in cogs1):
                bot.reply('Your request has been submitted.')
                bot.msg(operator, trigger.nick + ' has requested an invasion of ' + words[0])
            else:
                bot.msg(trigger.nick, 'Please use the correct name for the cog, try again in one minute. a list can be found http://pastebin.com/3FxNti9T')
    else:
        bot.msg(trigger.nick, 'Please include a cog name!')

    
