a=float(input("Enter Cost Price: "))
b=float(input("Enter selling price: "))
profit=b-a
loss=a-b
if a==0 or b==0:
    print("Enter valid value")
elif a<b:
    print(f"Profit is of{profit/a*100}%")
else:
    print(f"Loss is of{loss/a*100}%")