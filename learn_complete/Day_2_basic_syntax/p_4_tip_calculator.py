#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("*"*5+" Welcome to Bill Spliter "+"*"*5)

bill_amount = float(input("Billing Amount: ₹"))
tip_percentage = int(input("Tip Options 10, 12 or 15 (in %): "))
split_into = int(input("How many people to split the bill?\n"))

# tip_amount = bill_amount * (tip_percentage / 100)
# final_bill_amount = bill_amount + tip_amount

# or the pro maths version

final_bill = bill_amount * (1 + tip_percentage / 100)

pay_each = round(final_bill / split_into, 2)
pay_each = "{:.2f}".format(pay_each)
# print("%.2f" % pay_each)
print("*"*5+f" Each person: ₹{pay_each} "+"*"*5)
