
height = int(input("Height (in cm): "))

if height >= 120:
    print("Ride")
    age = int(input("Age (in years): "))
    if age <= 12:
        print("Pay: ₹50")
    elif age <= 20:
        print("Pay: ₹100")
    else:
        print("Pay: ₹200")
else:
    print("No Ride")
