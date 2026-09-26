print("1 for addition,2 for subtraction,3 for multiplication,4 for remainder,5 for division")

a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("which operation do you want to perform"))
if c==1 or c==2 or c==3 or c==4 or c==5 :

 if c==1 :

    print(a+b)
 elif c==2:
    print(a-b)
 elif c==3:
    print(a*b) 
elif c==4 :
    print(a%b)
elif c==5 :
    print(a/b)
else:
    print("beta tmse na ho payega")