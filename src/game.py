def game():
    print("Welcome to the Adventure Game!")
    print("You are inside your car. There are two choices, choose one of them for the adventure to start.")

    Choices = ["1: Take the left", "2: Tak right"]

    for choice in Choices:
        print (choice)

    valid_Choices = ["1", "2"]

    while True:
        choice = input("what is your choice")   
        if choice in valid_Choices:
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
        choice = input("What is your choice")
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
    print("You find somebody in the side of the rod and its car broke down")            

    Choices = ["1: You help him", "2: You continue"]

    for choice in Choices:
        print(choice)

    Valid_Choices = ["1", "2"]
    while True:
        choice = input("What is your choice:")
        if choice in Valid_Choices:    
            if choice == "1":
                print("You got the car fixed and you won 20 points")
            elif choice == "2":
                print("Your car runs out of gas")
                print("Since you are in the middle of nowhere, you lost the game")
            break
        else:
            print("Invalid Choice!"
    )

game()

