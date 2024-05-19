print("Welcome To The Treasure Island, Your task is to find the treasure")
print("You have only two ways to select i.e. left or right")
print("Please select your path: left or right ")
path = input()
if path != "left":
    print("You fell into a hole.\n Game Over")
else:
    print("You reached next point. Do you want to swim or wait?")
    next_path = input()
    if next_path != "wait":
        print("You got attacked by a trout.\n Game Over")
    else:
        print("You Reached next point, select a door to win.\tRed \tBlue \tYellow \tGreen")
        color = input()
        color = color.lower()
        if color == "yellow":
            print("You won the game")
        elif color == "red" or color == "Blue":
            if color == "red":
                print("Burned by Fire.\nGame Over")
            else:
                print("Eaten by beasts.\nGame Over")
        else:
            print("Game Over")
