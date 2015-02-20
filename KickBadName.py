import willie.module

"""
do not view below unless you will be mature!
do not view below unless you will be mature!
do not view below unless you will be mature!
do not view below unless you will be mature!
do not view below unless you will be mature!
do not view below unless you will be mature!
do not view below unless you will be mature!
do not view below unless you will be mature!
do not view below unless you will be mature!
do not view below unless you will be mature!
do not view below unless you will be mature!
do not view below unless you will be mature!
do not view below unless you will be mature!
do not view below unless you will be mature!
"""


bad_words = [
    'anus', 'arse', 'ass', 'basta', 'bitch', 'bone', 'butt', 'cock',
    'cunt', 'cracker', 'damn', 'dick', 'dike', 'dild', 'dyke', 'fag',
    'fuck', 'gay', 'hell', 'handjo', 'jizz', 'kunt', 'lesb', 'mcfagget', 
    'negro', 'nigg', 'nutsack', 'pecker', 'penis', 'piss', 'pussy',
    'prick', 'queer', 'renob', 'rimjob', 'shit', 'shiz', 'slut',
    'testicle', 'tit', 'twat', 'vaj', 'vag', 'wank', 'whore']

@willie.module.event('JOIN')
@willie.module.rule('.*') #needs to be here
def join(bot, trigger):
    #bot MUST be operator in channel for kick to take place
    reason = 'Please use a family friendly name!'
    name = trigger.nick.lower()
    if any(s in name for s in bad_words):
        bot.msg('Chanserv', 'KICK ' + trigger.sender + ' ' + trigger.nick + ' ' + reason)
