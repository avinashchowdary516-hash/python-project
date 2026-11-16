#hospital billing system
consultation = int(input("Enter consultation charge: "))
test = int(input("Enter test charge: "))
treatment = int(input("Enter treatment charge: "))

total = consultation + test + treatment

if total >= 5000:
    discount = total * 0.10
else:
    discount = 0

final_bill = total - discount

print("Total Bill =", total)
print("Discount =", discount)
print("Final Bill =", final_bill)