# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# concatenate and make it to lowercase all
complete_name = name1.lower() + name2.lower()

# count and add the characters from "True Love"
part_one = complete_name.count("t") + complete_name.count("r") + complete_name.count("u") + complete_name.count("e")
part_two = complete_name.count("l") + complete_name.count("o") + complete_name.count("v") + complete_name.count("e")

# love = part_one*10 + part_two 
# or
# con-catenate both the numbers
love = int(f"{part_one}{part_two}")

# compare and give output
if love <= 10 or love >= 90:
    print(f"Your score is {love}, you go together like coke and mentos.")
elif love >= 40 and love <= 50:
    print(f"Your score is {love}, you are alright together.")
else:
    print(f"Your score is {love}.")
