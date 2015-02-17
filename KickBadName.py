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




@willie.module.event('JOIN')
@willie.module.rule('.*') #needs to be here
def join(bot, trigger):
    #bot MUST be operator in channel for kick to take place
    reason = 'Please_use_a_family_friendly_name!'
    bad_words = [
        'anus', 'arse', 'ass', 'basta', 'bitch', 'bone', 'butt', 'cock',
        'cunt', 'cracker', 'damn', 'dick', 'dike', 'dild', 'dyke', 'fag',
        'fuck', 'gay', 'hell', 'handjo', 'jizz', 'kunt', 'lesb', 'mcfagget', 
        'negro', 'nigg', 'nutsack', 'pecker', 'penis', 'piss', 'pussy',
        'prick', 'queer', 'renob', 'rimjob', 'shit', 'shiz', 'slut',
        'testicle', 'tit', 'twat', 'vaj', 'vag', 'wank', 'whore'
        ]
    if any(s in trigger.nick for s in bad_words):
        bot.write(['KICK', trigger.sender, trigger.nick, reason])
