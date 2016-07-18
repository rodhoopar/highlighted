#!/usr/bin/env python

# helper script to parse player names and corresponding wikipedia pages from 
# https://en.wikipedia.org/wiki/List_of_current_NBA_team_rosters

import urllib2
import re
from unidecode import unidecode

link = "https://en.wikipedia.org/wiki/List_of_current_NBA_team_rosters"

# get html from link 
response = urllib2.urlopen(link)
html = response.read()

# find all players and their urls
raw_players = re.findall(r"<td style=\"text-align:left;\"><a href=.*?</td>(?!\n</tr>)", html)

players = [] # list of players
wiki_suffix_map = {} # map of player names to wikipedia suffixes

for player in raw_players:
	# parse url out of the html
	url = re.sub(r'<td style="text-align:left;"><a href="/wiki/', "", player)
	url = re.sub(r'".*?</td>', "", url)

	# parse player name out of the html 
	player = re.sub(r'<td style="text-align:left;"><a href=".*?" title=".*?">', "", player)
	player = re.sub(r'</a>.*?</td>', "", player)
	
	# use unidecode library to replace characters with accents with their regular version
	# e.g. 'á' becomes 'a'
	player = unicode(player, 'utf-8')
	player = unidecode(player)
	
	# reorder name to (first last) instead of (last, first)
	names = player.split(',')
	try:
		player = names[1].strip() + " " + names[0]
	# watch out for players with only one name
	except Exception:
		player = names[0]
	
	players.append(player)
	wiki_suffix_map[player.lower()] = url

# print the list and map
# works well because python lists and maps have similar syntax to JS arrays and objects, respectively
print players
print wiki_suffix_map