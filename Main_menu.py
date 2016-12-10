#Main menu that selects the game that you want to pull prices from
#Working on TF2 first since it's my favorite game and I understand TF2's market the most
Team_Fortress_2 = 1
Counter_Strike_Global_Offensive = 2
Dota_2 = 3

print ("What game do you want to list?")
print ("Team Fortress 2 = 1, Counter Strike: Global Offensive = 2, Dota 2 = 3")
Game_selector = input()
if Game_selector == "1":
 import TF2_SCM
elif Game_selector == "2":
  import CSGO_SCM
elif Game_selector == "3":
  import Dota2_SCM
else:
    print ("Please select a listed game")
