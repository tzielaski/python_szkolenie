grades = (2, 3, 3.5, 4, 4.5, 5)

grades_list = [float(grade) for grade in grades]

user_grades = []

while True:
    grade = input('Grade: ')

    if not grade:
        # if user hit enter, without typing number
        break
    else:
        grade = float(grade)
        if grade not in grades_list:
            print("Grade not allowed")
        else:
            user_grades.append(grade)

sum_grades = 0
for grade in user_grades:
    sum_grades += grade

mean_grade = sum_grades/len(user_grades)

print(f'Mean grade: {mean_grade}')