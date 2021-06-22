# program to play Rock, Paper and Scissor
# those who won will get prize

# rules
# user has to give three tries to compete with computer
# and must have to win all of them
# if user fails in anyone of the tries, gameover at that instant
# in another words user must have to score 3 / 0


# to import random library
import random 

print("Welocme to Rock Paper Scissor")
print("R -> Rock P -> Paper S -> Scissor")
letters = ['r','p','s']
winning_chances = 0

def take_input(wc):
  user = input("Choose: ").lower()
  computer = 's'
  # computer = random.choice(letters)
  print(user+" "+computer)
  wc += int(computer_the_outcomes(user, computer))
  return wc

def computer_the_outcomes(user_choice, computer_choice):
  score = 0
  if user_choice == computer_choice:
    print("Its draw")
  elif user_choice == 'r' and computer_choice == 'p':
    print("Game Over")
    return score
  elif user_choice == 'r' and computer_choice == 's':
    score = 1
    print("You think you're lucky...")
    return take_input(score)
  elif user_choice == 'p' and computer_choice == 'r':
    score = 1
    print("You think you're lucky...")
    return take_input(score)
  elif user_choice == 'p' and computer_choice == 's':
    print("Game Over")
    return score
  elif user_choice == 's' and computer_choice == 'r':
    print("Game Over")
    return score
  elif user_choice == 's' and computer_choice == 'p':
    score = 1
    print("You think you're lucky...")
    return take_input(score)
    
  return score
  


winning_chances += take_input(winning_chances)
if(winning_chances == 3):
  print(f"Your Score: {winning_chances}")
  print('''
    ________________ _     _____      _______________        ________   ___
  ,' ________   ___// \    \  __`-.  /___   ___/\  __`-.   ,' ___/\ /  ,' /
 |  `-.__    | |   / . \   | |,',-'      | |    | |,',-'  | ,'___ | |,',-'
  `-.___ `,  | |  / /_\ \  |  _ `-,      | |    |  _ `-,  |  ___/ |  _ `-,
  ______\  \ | | / _____ \ | | `-. \_    | |    | | `-. \_| `.___ | | `-. \_
 /_________| /_|/_/     \_\|_\   /__/    /_\    |_\   /__/ `.____||_\   /__/
''')


# import random
# import math

# def play():
#     user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
#     user = user.lower()

#     computer = random.choice(['r', 'p', 's'])

#     if user == computer:
#         return (0, user, computer)

#     # r > s, s > p, p > r
#     if is_win(user, computer):
#         return (1, user, computer)

#     return (-1, user, computer)

# def is_win(player, opponent):
#     # return true is the player beats the opponent
#     # winning conditions: r > s, s > p, p > r
#     if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
#         return True
#     return False

# def play_best_of(n):
#     # play against the computer until someone wins best of n games
#     # to win, you must win ceil(n/2) games (ie 2/3, 3/5, 4/7)
#     player_wins = 0
#     computer_wins = 0
#     wins_necessary = math.ceil(n/2)
#     while player_wins < wins_necessary and computer_wins < wins_necessary:
#         result, user, computer = play()
#         # tie
#         if result == 0:
#             print('It is a tie. You and the computer have both chosen {}. \n'.format(user))
#         # you win
#         elif result == 1:
#             player_wins += 1
#             print('You chose {} and the computer chose {}. You won!\n'.format(user, computer))
#         else:
#             computer_wins += 1
#             print('You chose {} and the computer chose {}. You lost :(\n'.format(user, computer))

#     if player_wins > computer_wins:
#         print('You have won the best of {} games! What a champ :D'.format(n))
#     else:
#         print('Unfortunately, the computer has won the best of {} games. Better luck next time!'.format(n))


# if __name__ == '__main__':
#     play_best_of(3) # 2
