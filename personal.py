#A keyboard adventure game

#Initialization

def init():
    print('********WELCOME TO STAFER DEN!******** \n********YOUR MIGHT SHALL BE TESTED!********')

    decision = input("********DO YOU HAVE WHAT IT TAKES?******** \n>>>I DO\n>>>I AM A WIMP\n")

    if decision.upper() == "I AM A WIMP":
        print("You suck! Go home")
    elif decision.upper() == "I DO":
        print('********Your Journey Starts Here********')
    else:
        print('INVALID SELECTION \n RETURN WHEN YOU LEARN TO READ')


#Creating pathways

def doors():
    door = input("Pick a door: \n >>>WOODEN DOOR \n>>>METAL DOOR \n")

    if door.upper() == 'WOODEN DOOR':
        print('Slowly, the door creaks open')
    elif door.upper() == 'METAL DOOR':
        print('The air is filled with heavy bolt sounds as the door opens')
    else:
        print('That door odes not exist')