a=int(input("Enter the number "))
if a%5==0 and a%11==0:
    print("The number is divisible by both 5 and 11")
elif a%5==0 and a%11 !=0:
    print("the number is divisible by only 5")
elif a%5!=0 and a%11 ==0:
    print("the number is divisible by 11")
else:
    print("the number is neither divisible by 11 nor 5")