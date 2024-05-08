from readmeimport import stuff
import time
import sys
    

x = input("whats the speed of your text? (slow, medium, fast)")
if x == "slow":
  def print_slow(str):
      for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.005)
    
if x == "medium":
  def print_slow(str):
      for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.0005)
      
if x == "fast":
  def print_slow(str):
      for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.00004)

class player: 
  
  def intro():
    x = input
    information = ('Welcome to Object Orientated Aventures! In this game, you will progressivley fight abominations in order to survive.   Each abomination has different stats, characteristics, and may drop useful items. Your goal is to defeat the three dungeons and then the final boss in order to escape. (Dont forget to upgrade our stts in the shop!) Here is some infornmation that can help you on your journey:')
    playername = input('What is the name of your Adventurer?:')
    print_slow(f"Welcome! {playername} to the world of Final Fantasy 178²")
    infoquestion = input('Would you like to read the manual? (Y/N) :')
    if infoquestion == 'Y':
       
     
      infoquestion = input("input space to continue")
    if infoquestion == " ":
          
          print("                                                                                                                                                               ") 
          print_slow("Here is some useful data:")
          print_slow(stuff)
          start = input('Type START to begin: ')


          if start == 'start' or 'START':
           print_slow("Good Luck")

player.intro()


"""
    def statsinv():
      import random
      hp = 100
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
      inventory = ["Potions-"[potioncount], "Big Potions-"[bigpotioncount]]"""



