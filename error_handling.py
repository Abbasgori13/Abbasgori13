data_valid = False

while data_valid == False:
    grade1 = input("Type the grade of first test: ")
    try:
        grade1 = float(grade1)
    except:
        print("Grade of first test is not valid")
        continue
    if grade1 < 0 or grade1 > 10:
        print("Grade should be between 0 to 10")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    grade2 = input("Type the grade of second test: ")
    try:
        grade2 = float(grade2)
    except:
        print("Grade of second test is not valid")
        continue
    if grade2 < 0 or grade2 > 10:
        print("Grade should be between 0 to 10")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    total_classes = input("Type the total number of classes: ")
    try:
        total_classes = int(total_classes)
    except:
        print("Invalid input for total classes")
        continue
    if total_classes <= 0:
        print("The number of classes cannot be zero or less")
        continue
    else:
        data_valid = True

data_valid = False

while data_valid == False:
    absences = input("Type the number of absences: ")
    try:
        absences = int(absences)
    except:
        print("Invalid input for total number of absences")
        continue
    if absences < 0 or absences > total_classes:
        print("The number of absences cannot be less than zero or greater that total number of classes")
        continue
    else:
        data_valid = True

avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences) / total_classes

print("Average grade: ", round(avg_grade,2))
print("Attendance rate: ", str(round((attendance * 100),2))+'%')

if (avg_grade >=6 and attendance >= 0.8):
    print("The student has been approved.")
elif(avg_grade < 6 and attendance < 0.8):
    print("The student has failed due to low grade and low attendance")
elif(attendance >= 0.8):
    print("The student has failed due to low grade")
else:
    print("The student has failed due to low attendance")