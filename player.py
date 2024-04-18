from readmeimport import stuff
import time

class player: 
    def intro():
     information = ('Welcome to Object Orientated Aventures! In this game, you will progressivley fight abominations in order to survive.   Each abomination has different stats, characteristics, and may drop useful items. Your goal is to defeat the three dungeons and then the final boss in order to escape. (Dont forget to upgrade our stts in the shop!) Here is some infornmation that can help you on your journey:')
     playername = input('What is the name of your Adventurer?:')
     print(f"Welcome! {playername} to the world of Final Fantasy 178²")
     infoquestion = input('Would you like to read the manual? (Y/N) :')
     if infoquestion == 'Y':
        print("                                                                                                                                                               ") 
        print(information) 
        infoquestion = input("input space to continue")
        if infoquestion == " ":
          time.sleep
          print("                                                                                                                                                               ") 
          print("Here is some useful data:")
          print(stuff)
     start = input('Type START to begin: ')
     print("                                                                                                                                                               ") 
     print("Here is some useful data:")
     print(stuff)
     start = input('Type START to begin:')
     if start == 'start' or 'START':
      print("Good Luck")
    def statsinv():
      import random
      hp = 100
      gold = 0
      upg = 0
      if upg == 0:
       dmg = int(random.randint(5,7))
      elif upg == 1:
        dmg = int(random.randint(7,9))
      elif upg == 2:
        dmg = int(random.randint(9,11))
      elif upg == 3:
        dmg = int(random.randint(11,13))
      potioncount = 0
      bigpotioncount = 0

      upgradeprice = 25
    def shopinteract(playername,upgradeprice,gold,potioncount, bigpotioncount,upg):
      print(f"Welcome to the Shop {playername}")
      shopquestion = input(f"What do you wish to buy? (Potion - 15, Big Potion - 60, upgrade{upgradeprice}) or exit:")
      if shopquestion == 'Potion' or shopquestion =="potion":
        gold - 15
        if gold<0:
          print("You do not have enough gold!")
          gold + 15
        potioncount + 1
        print("You bought a Potion!")
      elif shopquestion == 'Big Potion' or shopquestion == 'BigPotion' or shopquestion == 'bigpotion' or shopquestion =='big potion':
        gold - 60
        if gold<0:
          print("You do not have enough gold!")
          gold + 60
        bigpotioncount + 1
      elif shopquestion == "Upgrade" or shopquestion == "upgrade":
        gold - upgradeprice
        if gold<0:
          print("You do not have enough gold!")
          gold + upgradeprice
        upg + 1
        upgradeprice + 25

         
        




