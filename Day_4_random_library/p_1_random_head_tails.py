import random

coin_face = random.randint(0,1) 
print(coin_face)
if coin_face == 1:
    print("Head")
else:
    print("Tail")