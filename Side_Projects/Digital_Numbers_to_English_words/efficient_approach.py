upto_nineteen = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
upto_ninety = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
def to_words(number):
    word = ""
    if number < 20:
        word += upto_nineteen[number]
        return word
    elif number >= 20 and number < 100:
        word += upto_ninety[number // 10] + " " + upto_nineteen[number % 10]
        return word

def convert_number(digit):
    at_final = ""
    if digit > 0 and digit < 100:
        at_final += to_words(digit)
    elif digit >= 100 and digit < 1000:
        at_final += to_words(digit // 100) + " Hundred " + convert_number(digit % 100)
    elif digit >= 1000 and digit < 100000:
        at_final += to_words(digit // 1000) + " Thousand " + convert_number(digit % 1000)
    elif digit >= 100000 and digit < 10000000:
        at_final += to_words(digit // 100000) + " Lakh " + convert_number(digit % 100000)
    elif digit >= 10000000 and digit < 1000000000:
        at_final += to_words(digit // 10000000) + " Crore " + convert_number(digit % 10000000)
    else:
        at_final += "0 or less not valid input"
    return at_final
    
number = int(input("Enter Natural A Number: "))
print(convert_number(number))