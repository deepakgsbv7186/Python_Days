import random
deck = {
    "A" :11, "K": 10, "Q": 10, "J": 10,
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
}
# collect all the keys
cards = deck.keys()
# convert into list from dictionary
cards = list(cards)
# pick one random card with face
def deal_card():
    pick = random.choices(cards)[0]
    return deck[pick]

# initial start
computer = []
user = []
for _ in range(2):
    computer.append(deal_card())
    user.append(deal_card())  
print(f"{computer} {user}")

# return total points of both
def calculate_points(card_picks):
    points = 0
    for i in range(len(card_picks)):
        points += card_picks[i]
    return points
# print(f"c = {calculate_points(computer)}\nu = {calculate_points(user)}")


pick_again = False
user_points = 0
computer_points = 0
choice = input("Do you want another card(y/n): ")
if choice == "y":
    user.append(deal_card())  
    user_points += calculate_points(user)
    if user_points > 21:
        print(f"Busted Score: {user_points}")
        pick_again = True
else:
    computer_points += calculate_points(computer)
    if computer_points > 21:
        print(f"You Win, Computer Busted {computer_points}")
        pick_again = True
    elif computer_points < user_points:
        print(f"You Win, Computer Busted {computer_points}")
        pick_again = False
    else:
        computer.append(deal_card())
        pick_again = False
    