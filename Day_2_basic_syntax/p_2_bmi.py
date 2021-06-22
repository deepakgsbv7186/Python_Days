# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# conerted from string to int, float
weight_as_int = int(weight)
height_as_float = float(height)
# for squaring the height, use of ** as exponent

calculate_bmi = weight_as_int / height_as_float ** 2
# print the BMI as round off figure using int() typecast
print(int(calculate_bmi))

# home_work 
# using BMI chart show "what type they belong from?"