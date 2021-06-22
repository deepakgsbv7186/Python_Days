# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# if man live about 90 years 
# it might have ? days, ? weeks, ? months

# this is new me
age_as_int = int(age)
remaining_years = 90 - age_as_int

# now we are going to calculate left days, weeks and months of life

months_left = remaining_years * 12
weeks_left = remaining_years * 52
days_left = remaining_years * 365

# use of f_string in this line
to_print = f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left."

print(to_print)

# that was novice me
# assumed_months = 12 * 90
# assumed_weeks = 52 * 90
# assumed_days = 365 * 90

# current_months = 12 * int(age)
# current_weeks = 52 * int(age)
# current_days = 365 * int(age)

# left_months = assumed_months - current_months
# left_weeks = assumed_weeks - current_weeks
# left_days = assumed_days - current_days

# print(f"There are {left_days} days in a year, {left_weeks} weeks in a year and {left_months} months in a year.")

# now improved me
# coming sooner