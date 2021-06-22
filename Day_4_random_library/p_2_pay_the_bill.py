# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

# method using choice funtion with random
print(f"{random.choice(names)} is going to buy the meal today!")

# another method by using the values of list index
# names[2] like
# but to consider all the indexies in random.randint()
# as index start from zero to end of list

# calculate length of list for index
number_of_items = len(names)

# now generate random number between zero to end of list
random_choice = random.randint(0,number_of_items-1)

print(f"{names[random_choice]} is going to buy the meal today!")


