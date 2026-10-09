num=int(input("Enter Number"))
cube=0
while num>0:
    mod=num%10
    cube=cube+mod**2
    if cube==num:
        print("Armstrong Number")
    else:
        print("Not a armstrong number")
