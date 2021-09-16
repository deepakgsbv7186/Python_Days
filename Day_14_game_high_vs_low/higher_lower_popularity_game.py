import random, os, colorama
from art import logo, vs
from game_data import data

from colorama import Back
#initialize colorama package
colorama.init(autoreset=True)

def format_details(account):
    """fetch celebs details and format accordingly"""
    account_name = Back.MAGENTA+" Entity: "+account["name"]
    account_descp = Back.GREEN+" Profession: "+account["description"]
    account_country = Back.CYAN+" Belongs To: "+account["country"]
    # change font to appear more appealing(reminder)
    return f"{account_name}\n{account_descp}\n{account_country}"

def followers_comparsion(guess, celeb_a, celeb_b):
    """Here we get the arguments as followers count for each account
        and compare them for higher, also return the boolean value if user
        guessed right"""  
    if celeb_a > celeb_b:
        return guess == "a"
    else:
        return guess == "b" 

# display art
print(logo)
score = 0
game_on = True
account_b = random.choice(data)

# make the game repeatable
while game_on:
    # generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)

    # make possible that never gets same accounts
    while account_a == account_b:
        account_b = random.choice(data)
    # format the account data into printable order
    print(f"Compare To\n{format_details(account_a)}")
    print(vs)
    print(f"From\n{format_details(account_b)}")

    # ask user for a guess
    guess = input("Which is more popular (A or B): ").lower()

    # check if user is correct
        # get follower count of each accoaunt
    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]
        # use if statement to check if user is correct
    is_correct = followers_comparsion(guess,a_followers,b_followers)

    # clear the screen between rounds
    os.system("cls")
    # give user feedback on their guess
    if is_correct:
    # score must stored
        score += 1
        print(f"You're right. Score: {score}")
    else:
        game_on = False
        print(f"Final Score: {score} Sorry, Next Time!!!")


