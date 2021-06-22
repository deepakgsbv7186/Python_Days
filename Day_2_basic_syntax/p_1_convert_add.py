# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

# here we are going to separate using (subscripting method)
# also convert from string to int
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
# adding the numbers 
add = first_digit + second_digit
# final output we convert (add) to string
print("Your sum: "+str(add))