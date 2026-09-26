a=int(input("Enter the number "))
if a%3==0 and a%7==0:
    print("The number is divisible by both 3 and 7")
elif a%3==0 and a%7 !=0:
    print("the number is divisible by only 3")
elif a%3!=0 and a%7 ==0:
    print("the number is divisible by 7")
else:
    print("the number is neither divisible by 3 nor 7")