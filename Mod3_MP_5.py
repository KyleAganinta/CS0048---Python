
def calculateGrade(grades):
    for grade in grades:
        grade = (grade+grade)/len(grades)

while True:
    print(f"Welcome to grade calculator\n1. Add Score\n2. Calculate grade\n3.Exit")
    subList = []
    gradeList = []
    choice = int(input("Kindly input your choice: "))

    if choice == 1:
        subject = input("Input the subject: ")
        subList.append(subject)
        grade = input("Input the grade: ")
        subList.append(grade)

    if choice == 2:
        print(f"Your grade is {calculateGrade(gradeList)}")
    
    if choice == 3:
        break
        




