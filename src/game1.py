

def game():

    print("Welcome to the Adventure Game!")
    print("Choose your adventure")

    Choices = ["1:Carpool",
               "2: Dungeon",
               "3: Spaceship"]
    
    for choice in Choices:
        print(choice)

        valid_Choices = ["1", "2", "3"]
    while True:
        choice = input("What is your choice: ")
        if choice in valid_Choices:
            if choice == "1":
                Carpool()
            elif choice == "2":
                Dungeon()
            elif choice == "3":
                Spaceship()
            break    
        else:
            print("Invalid choice! Please enter either 1, 2 or 3")



def Carpool():

    print("You are inside your car. There are two choices, choose one of them for the adventure to start.")

    Choices = ["1: Take the left", "2: Tak right"]

    for choice in Choices:
        print (choice)

    valid_choices = ["1", "2"]
    while True:
        choice = input("what is your choice: ")   
        if choice in valid_choices:
            if choice == "1":
                left()
            elif choice == "2":
                right()
            break
        else:
            print("Invalid choice")


def left():   
    print("You choose to go left")
    print("You find people that need a ride")

    Choices = ["1: you give them a ride", "2: You continue without them"]

    for choice in Choices:
        print(choice)

    valid_choices = ["1", "2"] 
    while True:
        choice = input("What is your choice: ")
        if choice in valid_choices:
            if choice == "1":
                print("You drove them to their destination and you got 10 points") 
                print("Good job, if you win up to 50, you win the game.")
            elif choice == "2":
                print("You continued your adevnture, make sure to wwin some points next time.")
            break
        else:
            print ("Invalid choice. Enter either 1 or 2")         

def right():
    print("you went right")
    print("You find somebody in the side of the road and its car broke down")            

    Choices = ["1: You help him", "2: You continue"]

    for choice in Choices:
        print(choice)

    valid_choices = ["1", "2"]
    while True:
        choice = input("What is your choice: ")
        if choice in valid_choices:    
            if choice == "1":
                print("You got the car fixed and you won 20 points")
            elif choice == "2":
                print("Your car runs out of gas")
                print("Since you are in the middle of nowhere, you lost the game")
            break
        else:
            print("Invalid Choice!")




def Dungeon():
    print("You are in the room1: Which room are you going next")

    Options = ["Room 2: There is a monster inside",
                "Room 5:There is a pit"]

    for option in Options:
        print(option)

    valid_options = ["Room 2", "Room 5"]  
    while True:
        option = input("What is your option:")

        if option in Options:
            if option == "Room 2":
                print("You defeated the monster, you won!!!!")
            elif option == "Room 5":
                print("You fell in the pit!! AAAAAAAh you die")
            break    
        else:
            print("Invalid option!!!")       



def Spaceship():
    print("Welcome On board!!! Kiddo, Hope you are ready for the Adeventure")

    Directions = ["1: let's go to mars", "2: Let's go find Professor Advialo and get the money", "3: Let's explore the space"]

    for direction in Directions:
        print(direction)

    valid_directions = ["1", "2", "3"]   
    while True:
        direction = input("Choose your direction:")
        if direction in Directions:
            if direction == "1":
                print("Direction set to march, it will take around 1hour if we are full speed.")
            elif direction == "2":
                print("We have found the famous professor")
                print("Its bounty is enough to stop working. You won your retirement; no need to work again") 
            elif direction == "3":
                print("While exploring, you were atacked and the ship exploded. Everybody is dead!!!!!") 
            break    
        else:
            print("Invalid direction! Try again!!")

game()            





