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
    if digit < 100:
        at_final += to_words(digit)
        print(at_final)
    elif number >= 100 and number < 999:
        at_final += to_words(digit // 100) + " Hundred " + convert_number(digit % 100)
        print(at_final)
    
number = int(input("Enter Natural A Number: "))
convert_number(number)