student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
marks = 0
#TODO-2: Write your code below to add the grades to student_grades.👇
for student_name in student_scores:
    marks = student_scores[student_name]
    if marks > 90:
        student_grades[student_name] = "Outstanding"
    elif marks > 80:
        student_grades[student_name] = "Exceeds Expectations"
    elif marks > 70:
        student_grades[student_name] = "Acceptable"
    else:
        student_grades[student_name] = "Failed"
    

    

# 🚨 Don't change the code below 👇
print(student_grades)