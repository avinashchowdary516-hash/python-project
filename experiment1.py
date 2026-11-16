#university scholarship allocation
name = input("Enter student name: ")
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))
income = int(input("Enter family income: "))

if marks >= 80 and attendance >= 75 and income <= 200000:
    print("Eligible for Scholarship")
else:
    print("Not Eligible for Scholarship")