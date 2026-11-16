#railway fare calculator
age = int(input("Enter passenger age: "))
distance = int(input("Enter distance: "))

fare = distance * 2

if age >= 60:
    fare = fare * 0.80
elif age <= 12:
    fare = fare * 0.50

print("Railway Fare =", fare)