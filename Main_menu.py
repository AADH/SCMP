#Used to pull prices from the Steam Community Market
#Code is very messy and shitty, will fix later

import urllib.request

Team_Fortress_2 = 1
Counter_Strike_Global_Offensive = 2
Dota_2 = 3

Print "What game do you want to list?"
Print "Team Fortress 2 = 1, Counter Strike: Global Offensive = 2, Dota 2 = 3"
Game_selector = input()
if Game_selector == 1
 import TF2_SCM
 elif Game_selector == 2
  import CSGO_SCM
 elif Game_selector == 3
  import Dota2_SCM
 elif Game_selector <1
  print("Please input a listed game")
 else Game_selector >3
  print("Please input a listed game")

page = urllib.request.urlopen("")
