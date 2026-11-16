#student examination result
marks = []

for i in range(1, 6):
    m = int(input("Enter subject marks: "))
    marks.append(m)

total = sum(marks)
average = total / 5

print("Total Marks =", total)
print("Average =", average)

if all(m >= 35 for m in marks):
    print("Result: Pass")
else:
    print("Result: Fail")