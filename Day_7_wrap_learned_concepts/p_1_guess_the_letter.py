# select a word from given list randomly
import random
word_list = ["apple","pineapple","applepie"]
chosen_word = random.choice(word_list)
print(chosen_word)
# create a empty list
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += '_'
print(display)    

end_of_game = False
while not end_of_game:
    # take user guess input one letter only 
    # and convert into lower
    guess = input("Guess one letter: ").lower()
    # here we are going to check 
    # whether user guess letter is in this list

    for index in range(word_length):
        letter = chosen_word[index]
        if guess == letter:
            display[index] = guess
    print(display)
    if '_' not in display:
        end_of_game = True
        print("You Win")