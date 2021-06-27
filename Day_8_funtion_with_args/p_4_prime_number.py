#Write your code below this line 👇
def prime_checker(number):
    flag = False
    factor = []
    for counter in range(2,number):
        if (number % counter) == 0:
            flag = True
            # takes the counter value i.e factors Into the list
            factor.append(counter)
    if flag:
        print("It's not prime")
        print(f"Here are the factors: {factor}")
    else:
        print("It's a prime number")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
