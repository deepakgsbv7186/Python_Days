# program which generate digital numbers to english words

# take input with no negative and decimals
number = int(input("Input the positive natural number: "))

def to_word(one_digit):
    """ using words of list from zero to nine
    it returns the corresponding word for each digit input """
    number_words = ["one","two", "three","four","five","six","seven","eight","nine","zero"]
    return number_words[one_digit - 1]

# store all the numbers, with reverse order
number_list = []
# funtinonal for separating each digit 
while number != 0:
    digit = number % 10
    number_list.append(digit)
    number =int(number/10)
# reverse the list to get appropriate output
number_list.reverse()

# at last print the list with original order
for digit in number_list:
    print(to_word(digit))