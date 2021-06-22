# take input and convert from string to int
a = int(input("a: "))
b = int(input("b: "))

# method without using temporary variable
a = a + b
b = a - b
a = a - b

# now going to print results
# but we have to convert back to string format
# that print funtion works easily
print("a: "+str(a))
print("b: "+str(b))