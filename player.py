from readmeimport import stuff


class player: 
    def intro():
     information = ('Welcome to Object Orientated Aventures! In this game, you will progressivley fight abominations in order to survive.   Each abomination has different stats, characteristics, and may drop useful items. Your goal is to defeat the three dungeons and then the final boss in order to escape. (Dont forget to upgrade our stts in the shop!) Here is some infornmation that can help you on your journey:')
     playername = input('What is the name of your Adventurer?:')
     print(f"Welcome! {playername} to the world of Final Fantasy 178²")
     infoquestion = input('Would you like to read the manual? (Y/N) :')
     if infoquestion == 'Y':
       
        print("                                                                                                                                                               ") 
        print(information) 
        print("                                                                                                                                                               ") 
        print("Here is some useful data:")
        print(stuff)
     start = input('Type START to begin:')
     if start == 'start' or 'START':
      print("gl")
player.intro()



