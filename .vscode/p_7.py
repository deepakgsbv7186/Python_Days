number_upto_nine = {
    1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine",
}
number_eleven_to_nineteen = {
    11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 16 : "sixteen", 17 : "seventeen", 18 : "eighteen", 19 : "nineteen",
}
number_ten_to_ninety = {
    10 : "ten", 20 : "twenty", 30 : "thirty", 40 : "forty", 50 : "fifty", 60 : "sixty", 70 : "seventy", 80 : "eighty", 90 : "ninety",
}
# print(number_upto_nine[8]) 
# print(number_eleven_to_nineteen[18])
# print(number_ten_to_ninety[90] + number_upto_nine[6])
# take input with no negative and decimals
number = int(input("Input the positive natural number: "))

def to_word(one_digit):
    """ using several words of list 
    it returns the corresponding word for each digit input """
    if one_digit < 10 :
        return number_upto_nine[one_digit]
    elif one_digit < 20 :
        return number_eleven_to_nineteen[one_digit]
    else:
        return number_ten_to_ninety[one_digit]

# store all the numbers, with reverse order
number_list = []
# funtinonal for separating each digit 
if number < 10 and number > 0:
    print(to_word(number))
else:
    while number != 0:
        digit = number % 10
        try:
            number = int(number / 10)
        except ZeroDivisionError:
            number_list.append(digit)
            
        if number == 0:
            number_list.append(digit * 10)
        else:
            number_list.append(digit)
        
# reverse the list to get appropriate output
number_list.reverse()
less_than_twenty = sum(number_list)
if less_than_twenty > 10 and less_than_twenty < 20:
    print(to_word(less_than_twenty))
else:
    for digit in number_list:
        print(to_word(digit))