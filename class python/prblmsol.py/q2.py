a=int(input("Enter a number "))
if a>0 and a%2==0 :
    print("The number is postive and even")
elif a<0 and a%2==0:
    print("The number is negative and even")
elif a>0 and a%2==1:
    print("the number is odd and postive")
elif a<0 and a%2==0:
    print("The number is negative and even")
elif a<0 and a%2==1:
 print("the number is odd and negative")
else:
   print("the number is zero")
