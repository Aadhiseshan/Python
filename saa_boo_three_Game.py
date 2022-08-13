from random import randint

choice=['saa','boo','three']
computer=choice[randint(0,2)]

repeat='Y'

while repeat == 'Y':
    player = False

    while player == False:
        play=input("Enter your Choice SAA,BOO,THREE: ")

        if play == computer:
            print("You Win")
            player = True

        elif play != computer:
            print("You Loss")

        else:
            print("Check the Spelling")
    
    chioce=input("Enter the y or n for continue the Game: ")

    repeat =chioce.upper()

    if  repeat != 'Y':
        print("\n *******************************************************************")
        print("\n\t\t Thank for playing the Game")
        print("\n *******************************************************************")
