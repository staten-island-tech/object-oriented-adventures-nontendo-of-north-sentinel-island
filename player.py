from readmeimport import stuff
import time
import sys
    

class player:
    def __init__(self, name, max_hp=100):
        self.name = name
        self.max_hp = max_hp
        self.damage = 10
        self.gold = 25
        self.minor_potions = 0
        self.major_potions = 0
    








    
    
x = input("whats the speed of your text? (slow, medium, fast)")
if x == "slow":
  def print_slow(str):
      for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)
    
if x == "medium":
  def print_slow(str):
      for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.005)
      
if x == "fast":
  def print_slow(str):
      for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.000001)

class user: 
  
  def intro():
    from readmeimport import stuff
    x = input
    information = ('Welcome to Object Orientated Aventures! In this game, you will progressivley fight abominations in order to survive.   Each abomination has different stats, characteristics, and may drop useful items. Your goal is to defeat the three dungeons and then the final boss in order to escape. (Dont forget to upgrade our stts in the shop!) Here is some infornmation that can help you on your journey:')
    playername = input('What is the name of your Adventurer?:')
    print_slow(f"Welcome! {playername} to the world of Final Fantasy 178²")
    print("                                                                                                                                                               ") 
    infoquestion = input('Would you like to read the manual? (WARNING:ITS ALOT) (Y/N) :')
    if infoquestion == 'Y':
       
     
      infoquestion = input("input space to continue")
    if infoquestion == " ":
          
          print("                                                                                                                                                               ") 
          print_slow("Here is some useful data:")
          print("                                                                                                                                                               ") 
          print("                                                                                                                                                               ") 
          print_slow(stuff)
          start = input('Type START to begin: ')


          if start == 'start' or 'START':
            print("                                                                                                                                                               ") 
            print_slow("You attack by choosing a number between 1-3 and choosing the right number means you land a hit")
            print("                                                                                                                                                               ") 
            print_slow("Good Luck")

    if infoquestion == 'N':
       start = input('Type START to begin: ')
       if start == 'start' or 'START':
           print("                                                                                                                                                               ") 
           print_slow("You attack by choosing a number between 1-3 and choosing the right number means you land a hit")
           print("                                                                                                                                                               ") 
           print_slow("Good Luck")






