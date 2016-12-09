#Used to pull prices from the Steam Community Market
#Code is very messy, will fix later

import urllib.request

Game_selector = 0

Team_Fortress_2 = 1
Counter_Strike_Global_Offensive = 2
Dota_2 = 3


Print "What game do you want to list?"
while Game_selector = 
Print "Team Fortress 2 = 1, Counter Strike: Global Offensive = 2, Dota 2 = 3"
 i=input("")

Game_selector = int(i)

page = urllib.request.urlopen("")
