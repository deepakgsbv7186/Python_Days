number_upto_nine = {
    0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine",
}
number_eleven_to_nineteen = {
    11 : "eleven", 12 : "twelve", 13 : "thirteen", 14 : "fourteen", 15 : "fifteen", 16 : "sixteen", 17 : "seventeen", 18 : "eighteen", 19 : "nineteen",
}
number_ten_to_ninety = {
    10 : "ten", 20 : "twenty", 30 : "thirty", 40 : "forty", 50 : "fifty", 60 : "sixty", 70 : "seventy", 80 : "eighty", 90 : "ninety",
}


def to_word(one_digit):
    """ using several words of list 
    it returns the corresponding word for each digit input """
    if one_digit < 10 :
        return number_upto_nine[one_digit]
    elif one_digit < 20 and one_digit > 10 :
        return number_eleven_to_nineteen[one_digit]
    else:
        return number_ten_to_ninety[one_digit]

def order_digits():        
    # reverse the list to get appropriate output
    number_list.reverse()
    less_than_twenty = sum(number_list)
    if less_than_twenty > 10 and less_than_twenty < 20:
        print(to_word(less_than_twenty))
    else:
        for digit in number_list:
            if digit == 0:
                pass
            else:
                print(to_word(digit))

def separate_digit(number):
    # funtinonal for separating each digit 
    if number < 10 and number > 0:
        print(to_word(number))
    else:
        while number != 0:
            digit = number % 10
            number = int(number / 10)
            if number == 0:
                number_list.append(digit * 10)
            else:
                number_list.append(digit)
    order_digits()

number = int(input("Input the positive natural number: "))
# store all the numbers, with reverse order
number_list = []
separate_digit(number)