
import time
import sys
    




""" x = input("whats the speed of your text? (slow, medium, fast)")
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
else:
   print("Invalid Choice! Your text speed is instant now >:)") """



class user: 
  
  def intro():
    from readmeimport import stuff
    x = input
    information = ('Welcome to Object Orientated Aventures! In this game, you will progressivley fight abominations in order to survive.   Each abomination has different stats, characteristics, and may drop useful items. Your goal is to defeat the three dungeons and then the final boss in order to escape. (Dont forget to upgrade our stts in the shop!) Here is some infornmation that can help you on your journey:')
    playername = input('What is the name of your Adventurer?:')
    print(f"Welcome! {playername} to the world of Final Fantasy 178²")
    print("                                                                                                                                                               ") 
    infoquestion = input('Would you like to read the manual? (ITS ALOT but you can come back to it later) (Y/N) :')
    if infoquestion == 'Y':
       
     
      infoquestion = input("input space to continue")
    if infoquestion == " ":
          
          print("                                                                                                                                                               ") 
          print("Here is some useful data:")
          print("                                                                                                                                                               ") 
          print("                                                                                                                                                               ") 
          print(stuff)
          start = input('Type START to begin: ')


          if start == 'start' or 'START':
            print("                                                                                                                                                               ") 
            print("                                                                                                                                                               ") 
            print("Good Luck")

    if infoquestion == 'N':
       start = input('Type START to begin: ')
       if start == 'start' or 'START':
           print("                                                                                                                                                               ") 
           print("                                                                                                                                                               ") 
           print("Good Luck")






