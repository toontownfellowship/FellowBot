# coding=utf8
"""
youtube.py - Willie YouTube Module
Copyright 2012, Dimitri Molenaars, Tyrope.nl.
Copyright © 2012-2014, Elad Alfassa, <elad@fedoraproject.org>
Copyright 2012, Edward Powell, embolalia.net
Licensed under the Eiffel Forum License 2.

http://willie.dfbta.net

This module will respond to .yt and .youtube commands and searches the youtubes.
"""
from __future__ import unicode_literals, division
from willie import web, tools
from willie.module import rule, commands, example
import json
import re
import sys
if sys.version_info.major < 3:
    from HTMLParser import HTMLParser
else:
    from html.parser import HTMLParser

regex = re.compile('(youtube.com/watch\S*v=|youtu.be/)([\w-]+)')


def setup(bot):
    if not bot.memory.contains('url_callbacks'):
        bot.memory['url_callbacks'] = tools.WillieMemory()
    bot.memory['url_callbacks'][regex] = ytinfo


def shutdown(bot):
    del bot.memory['url_callbacks'][regex]


def ytget(bot, trigger, uri):
    bytes = web.get(uri)
    result = json.loads(bytes)
    try:
        if 'feed' in result:
            video_entry = result['feed']['entry'][0]
        else:
            video_entry = result['entry']
    except KeyError:
        return {'link': 'N/A'}  # Empty result

    vid_info = {}
    try:
        # The ID format is tag:youtube.com,2008:video:RYlCVwxoL_g
        # So we need to split by : and take the last item
        vid_id = video_entry['id']['$t'].split(':')
        vid_id = vid_id[len(vid_id) - 1]  # last item is the actual ID
        vid_info['link'] = 'http://youtu.be/' + vid_id
    except KeyError:
        vid_info['link'] = 'N/A'

    try:
        vid_info['title'] = video_entry['title']['$t']
    except KeyError:
        vid_info['title'] = 'N/A'

    #get youtube channel
    try:
        vid_info['uploader'] = video_entry['author'][0]['name']['$t']
    except KeyError:
        vid_info['uploader'] = 'N/A'

    #get views
    try:
        views = video_entry['yt$statistics']['viewCount']
        vid_info['views'] = str('{0:20,d}'.format(int(views))).lstrip(' ')
    except KeyError:
        vid_info['views'] = 'N/A'

    return vid_info


@rule('.*(youtube.com/watch\S*v=|youtu.be/)([\w-]+).*')
def ytinfo(bot, trigger, found_match=None):
    """
    Get information about the latest video uploaded by the channel provided.
    """
    match = found_match or trigger
    #Grab info from YT API
    uri = 'https://gdata.youtube.com/feeds/api/videos/' + match.group(2) + '?v=2&alt=json'

    video_info = ytget(bot, trigger, uri)
    if video_info is 'err':
        return
    bad_words = [
    'anus', 'arse', 'ass', 'basta', 'bitch', 'bone', 'butt', 'cock',
    'cunt', 'cracker', 'damn', 'dick', 'dike', 'dild', 'dyke', 'fag',
    'fuck', 'gay', 'hell', 'handjo', 'jizz', 'kunt', 'lesb', 'mcfagget', 
    'negro', 'nigg', 'nutsack', 'pecker', 'penis', 'piss', 'pussy',
    'prick', 'queer', 'renob', 'rimjob', 'shit', 'shiz', 'slut',
    'testicle', 'tit', 'twat', 'vaj', 'vag', 'wank', 'whore']
    title = video_info['title'].lower()
    if any(s in title for s in bad_words):
        reason = 'Bad word in youtube title!'
        bot.msg('Chanserv', 'KICK ' + trigger.sender + ' ' + trigger.nick + ' ' + reason)
        return

    #combine variables and print
    message = '[YouTube] Title: ' + video_info['title'] + \
              ' | Uploader: ' + video_info['uploader'] + \
              ' | Views: ' + video_info['views']
    
    bot.say(HTMLParser().unescape(message))


