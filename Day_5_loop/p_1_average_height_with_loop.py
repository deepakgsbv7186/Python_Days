# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# calculate length of the list
len = 0
sum = 0
for height in student_heights:
    len += 1
    sum += height

# now average = values of items / number of items
average_height = round(sum / len)

# result
print(f"Average Height: {average_height}")
