import willie.module

@willie.module.commands('request')
@willie.module.rate(30) #30 second cooldown for one user
def gt(bot, trigger):
    operator = '#TTFSinvasions' #this can also be a '#channel'
    words = trigger.group(2).split(' ')
    if len(words) >= 1:
        if len(words) == 3:
            cogs3 = ['mover and shaker', 'mover & shaker',
            'the big cheese', 'the big cheeses']
            cogname = words[0] + ' ' + words[1] + ' ' + words[2]
            if any(b == cogname for b in cogs3):
                bot.reply('Your invasion request has been submitted!')
                bot.msg(operator, trigger.nick + ' has requested an invasion of ' + words[0] + ' ' + words[1] + ' ' + words[2])
            else:
                bot.msg(trigger.nick, 'Please use the correct name for the cog! Try again in 30 seconds.  You can view a guide here: https://www.toontownfellowship.com/irc/')        
        elif len(words) == 2:
            cogs2 = ['cold caller', 'cold callers', 'name dropper', 'name droppers',
                'glad hander', 'glad handers', 'mover shaker', 'mover shakers',
                'two face', 'two faces', 'the mingler', 'the minglers',
                'mr hollywood', 'mr. hollywood', 'mr hollywoods', 'mr. hollywoods',
                'short change', 'short changes', 'penny pincher', 'penny pinchers',
                'bean counter', 'bean counters', 'number cruncher', 'number crunchers',
                'money bag', 'money bags', 'loan shark', 'loan sharks',
                'robber baron', 'robber barons', 'bottom feeder', 'bottom feeders',
                'double talker', 'double talkers', 'ambulance chaser', 'ambulance chasers', 
                'back stabber', 'back stabbers', 'spin doctor', 'spin doctors',
                'legal eagle', 'legal eagles', 'big wig', 'big wigs',
                'pencil pusher', 'pencil pushers', 'head hunter', 'head hunters',
                'corporate raider', 'corporate raiders', 'big cheese', 'big cheeses']
            cogname = words[0] + ' ' + words[1]
            if any(b == cogname for b in cogs2):
                bot.reply('Your invasion request has been submitted!')
                bot.msg(operator, trigger.nick + ' has requested an invasion of ' + words[0] + ' ' + words[1])
            else:
                bot.msg(trigger.nick, 'Please use the correct name for the cog! Try again in 30 seconds.  You can view a guide here: https://www.toontownfellowship.com/irc/')
        else:
            cogs1 = ['telemarketer', 'telemarketers', 'two-face', 'tightwad',
            'tightwads', 'bloodsucker', 'bloodsuckers', 'backstabber',
            'backstabbers', 'flunky', 'flunkys', 'flunkies',
            'yesman', 'yesmen', 'micromanager', 'micromanagers',
            'downsizer', 'downsizers']
            if any(a == words[0] for a in cogs1):
                bot.reply('Your invasion request has been submitted!')
                bot.msg(operator, trigger.nick + ' has requested an invasion of ' + words[0])
            else:
                bot.msg(trigger.nick, 'Please use the correct name for the cog! Try again in 30 seconds.  You can view a guide here: https://www.toontownfellowship.com/irc/')
    else:
        bot.msg(trigger.nick, 'Please include a cog name!  Try again in 30 seconds.  You can view a guide here: https://www.toontownfellowship.com/irc/')

    
