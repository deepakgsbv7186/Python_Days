# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# general information about program
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese

#Write your code below this line 👇

# calculation of Body Mass Index (BMI)
bmi_index = round(weight / height ** 2)
# print(cal_bmi_index)

# all the required condition to categoires
if bmi_index < 18.5:
    print(f"{bmi_index} Underweight")
elif bmi_index < 25:
    print(f"{bmi_index} Normal")
elif bmi_index < 30:
    print(f"{bmi_index} Slightly Overweight")
elif bmi_index < 35:
    print(f"{bmi_index} Obese")
else:
    print(f"{bmi_index} Clinically Obese")