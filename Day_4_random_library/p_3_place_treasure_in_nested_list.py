# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# # to separate row and column mathematically
# position = int(position)
# row = int(position / 10)
# col = position % 10
# # now first select row and then put "#" on column
# select_position = map[row - 1]
# select_position[col - 1] = "#"

# do it like pro in one line
map[int(position[0]) - 1][int(position[1]) - 1] = "#"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")