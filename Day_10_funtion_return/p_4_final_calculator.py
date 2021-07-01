
def add (n1, n2):
    """ add two numbers """
    return n1 + n2
def subtract (n1, n2):
    """ subtract two numbers """
    return n1 - n2
def multiply (n1, n2):
    """ multiply two numbers """
    return n1 * n2
def divide (n1, n2):
    """ divide two numbers """
    return n1 / n2
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
from art import logo
print(logo)
# take input first input
num1 = float(input("First Number: "))
all_symbols = ""
for symbol in operations:
    all_symbols += symbol + "  "
# print(f"Opertions: {all_symbols}")

again = False
while not again:
    print(f"Opertions: {all_symbols}")
    operation_symbol = input("Perform: ")
    num2 = float(input("Next Number: "))

    # perform function
    funtion = operations[operation_symbol]
    answer = funtion(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    # ask to continue
    choose = input("Press 'y' to continue or 'n' to end: ").lower()
    if choose == "y":
        num1 = answer
    else:
        again = True
        print("End of Program")
