
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

num1 = int(input("First Number: "))
all_symbols = ""
for symbol in operations:
    all_symbols += symbol + "  "
print(f"Opertions: {all_symbols}")
operation_symbol = input("Perform: ")
num2 = int(input("Second Number: "))
funtion = operations[operation_symbol]
answer1 = funtion(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer1}")

# take result from above and perform new calculation
print(f"Opertions: {all_symbols}")
operation_symbol = input("Perform: ")
next_num = int(input("Next Number: "))
funtion = operations[operation_symbol]
answer2 = funtion(answer1, next_num)
print(f"{answer1} {operation_symbol} {next_num} = {answer2}")


