#tuple based employee details
employees = [
    (101, "Ravi", 25000),
    (102, "Kiran", 30000),
    (103, "Sita", 28000)
]

for emp in employees:
    emp_id, name, salary = emp
    print("Employee ID:", emp_id)
    print("Name:", name)
    print("Salary:", salary)
    print("----------------")