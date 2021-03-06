# highlighted

Source code for the Chrome extension highlighted, which highlights the names of active NBA players found in the pages you browse. When you hover over the name, the extension will display a small popup that has the player's information and statistics from Wikipedia. Useful tool to help out with fantasy basketball, for example :)

Demo of capabilities: 

![Screenshot](https://raw.github.com/rodhoopar/highlighted/master/examples/demo.png)

Also included is a python script that I wrote to get the names and corresponding Wikipedia URL's of all current NBA players from [https://en.wikipedia.org/wiki/List_of_current_NBA_team_rosters](https://en.wikipedia.org/wiki/List_of_current_NBA_team_rosters). I wrote it because I couldn't find a list of NBA players as strings; it works by outputting the python list of players and map of players to URL's as a JavaScript array and object, respectively. 

In future versions I hope to expand to more sports/leagues. Uses the highlight and tipped extensions to jQuery.
