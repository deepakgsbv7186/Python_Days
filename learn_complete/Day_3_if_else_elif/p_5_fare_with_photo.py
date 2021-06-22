
height = int(input("Height (in cm): "))

if height >= 120:
    age = int(input("Age (in years): "))
    if age <= 12:
        bill = 50
        print("Current Pay: ₹50")
    elif age <= 20:
        bill = 100
        print("Current Pay: ₹100")
    else:
        bill = 200
        print("Current Pay: ₹200")
    
    # place an option for photo
    with_photo = input("Do you want take photo?(y/n): ")
    if with_photo == 'y':
        bill += 20
    
    print(f"Your Total Bill: {bill}")
else:
    print("No Ride")
