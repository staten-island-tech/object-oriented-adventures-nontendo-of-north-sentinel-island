class player: 
    def intro():
     information = ('messi')
     playername = input('What is the name of your Adventurer?:')
     print(f"Welcome! {playername} to the world of Final Fantasy 178²")
     infoquestion = input('Would you like to read the manual? (Y/N) :')
     if infoquestion == 'Y':
        print(information)
     start = input('Type START to begin:')
     if start == 'start'.lower() or 'START'.upper():
        print('placeholder')
     else:
        exit

player.intro()



