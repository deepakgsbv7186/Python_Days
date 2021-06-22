import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
play_images = [rock, paper, scissors]

user_guess = int(input("1 -> Rock 2 -> Paper 3 -> Scissors\n"))
computer_guess = random.choice([1,2,3])
if user_guess > 3 or user_guess <= 0:
    print("BBBAAADDD ENTry")
else:
    print(f"{play_images[user_guess - 1]} \n \n {play_images[computer_guess - 1]}")
    if user_guess == computer_guess:
        print("Draw")
    elif (user_guess == 1 and computer_guess == 3) or (user_guess == 2 and computer_guess == 1) or (user_guess == 3 and computer_guess == 2):
        print("You win")
    else:
        print("Lose the game")
