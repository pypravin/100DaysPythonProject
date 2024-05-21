import random as rand
output =['''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
SCISSOR
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
user_input = 0
random_num = rand.randint(0,2)
print("Welcome to Rock Paper Scissor Game.\n You will be playing this game against the computer")
print("Enter 0 for Rock, 1 for Paper, 2 for Scissor")
user_input =int(input())
if user_input>=0 and user_input<=2:
    print(output[user_input])
    print(output[random_num])
    if(user_input == random_num):
        print("Draw")
    elif(user_input == 0):
        if(random_num==2):
            print("You Won")
        else:
            print("you loose")
    elif(user_input == 1):
        if(random_num ==0):
            print("You Won")
        else:
            print("you loose")
    elif(user_input == 2):
        if(random_num == 1):
            print("You Won")
        else:
            print("you loose")
