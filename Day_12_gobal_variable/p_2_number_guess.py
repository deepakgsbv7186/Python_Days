# display game logo
from art import logo
print(logo)
# generate a random number range (1,100)
from random import randint
computer_choose = randint(1,100)
print(computer_choose)
def compare_with(choose,level):
    ''' take random generated number and difficulty level,
        depending on level they get chances to guess '''
    finish = False
    if level == "h":
        lives = 3
    else:
        lives = 5
    while not finish:
        print(f"You have {lives} chances left.")
        lives -= 1
        guess_by_user = int(input("Enter Number: "))
        if lives <= 0:
            finish = True
            return "You Lose The Game"
        elif guess_by_user == choose:
            finish = True
            return "You Win"
        elif guess_by_user > choose:
            print("High")
        elif guess_by_user < choose:
            print("Low")

# take input for difficulty level
diff_level = input("H -> Hard or L -> Low: ").lower()
# now function call 
print(compare_with(computer_choose,diff_level))
