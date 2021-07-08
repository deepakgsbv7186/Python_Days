upto_nine = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
upto_nineteen = ["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
upto_ninety = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
number = int(input("Enter Natural A Number: "))
if number > 99999999:
    print("No records.")
else:
    digits = [0,0,0,0,0,0,0,0]
    i = 0
    in_words = ""
    while number > 0:
        digits[i] = number % 10
        i += 1
        number = number // 10
    if digits[7] != 0:
        in_words += upto_nine[digits[7]] + " Crore "
    if digits[6] != 0:
        if digits[6] == 1:
            in_words += upto_nineteen[digits[5]] + " Lakh "
        else:
            in_words += upto_ninety[digits[6]] + " " +  upto_nine[digits[5]] + " Lakh "
    else:
        if digits[5] != 0:
            in_words += upto_nine[digits[5]] + " Lakh "
    if digits[4] != 0:
        if digits[4] == 1:
            in_words += upto_nineteen[digits[3]] + " Thousand "
        else:
            in_words += upto_ninety[digits[4]] + " " + upto_nine[digits[3]] + " Thousand "
    else:
        if digits[3] != 0:
            in_words += upto_nine[digits[3]] + " Thousand "
    if digits[2] != 0:
        in_words += upto_nine[digits[2]] + " Hundred "
    if digits[1] != 0:
        if digits[1] == 1:
            in_words += upto_nineteen[digits[0]]
        else:
            in_words += upto_ninety[digits[1]] + " " + upto_nine[digits[0]]
    else:
        in_words += upto_nine[digits[0]]
    print(in_words)