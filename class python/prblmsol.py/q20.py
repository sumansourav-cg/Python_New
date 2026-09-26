a=int(input("enter the first side"))
b=int(input("enter the second side"))
c=int(input("enter the Third side"))
if a==b==c:
    print("equilateral triangle")
elif a==b or a==c or b==c:
    print("isoceles triangle")
else:
    print("Saclene triangle")