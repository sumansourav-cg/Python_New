a=int(input("Enter first side"))
b=int(input("Enter second side"))
c=int(input("Enter third side"))
if a+b>c or a+c>b or b+c>a:
    print("Valid triangle")
else:
    print("Invalid triangle")
    