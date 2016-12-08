#Used to pull prices from the Steam Community Market

import urllib.request

Team_Fortress_2 = 1
Counter_Strike_Global_Offensive = 2
Dota 2 = 3

Print "What game do you want to list?"
Print "Team Fortress 2 = 1, Counter Strike: Global Offensive = 2, Dota 2 = 3"

page = urllib.request.urlopen("")
