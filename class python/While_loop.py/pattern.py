# n=int(input("Enter number"))
# if n==2 :
#    print("prime Number")
# elif n==1:
#    print("Not Prime") 
# else:
    

#   for i in range(2,n):
    
#       if n%i!=0 :
#         print("Prime Number")
#         break
    
      
#       else:
#         print("non-prime Number")
#         break
# weekday=int(input("Enter Weekday "))
# match weekday:
#     case 1|2|3|4|5:
#         print("Weekday")
#     case 6|7:
#         print("Weekend")

# marks=int(input("Enter marks "))
# match marks:
#     case x if x>90:
#         print("A")
#     case x if x>80:
#         print("B")
#     case x if x>70:
#         print("C")
#     case x if x>60:
#         print("D")
#     case x if x>50:
#         print("E")
#     case _:
#         print("Fail")

    
# num1=int(input("Input Number 1 to 3 to check options"))
# match num1:
#   case 1:
#     print("Check Acc Balance")
#     num2=int(input("Enter 4 for current acc or enter 5 for saving acc or enter 6 for joint acc"))
#     match num2:
#       case 4:
#         print("Current acc")
#       case 5:
#         print("Saving acc")
#       case 6:
#         print("Joint acc")

#   case 2:
#     print("Check flight status")
#     num3=int(input("Enter 7,8,9 for flight status , when flight will take off and when flight will land"))
#     match num3:
#       case 7:
#         print("Today")
#       case 8:
#         print("Tomorrow")
#       case 9:
#         print("Day after tomorrow")   
#   case 3:
#     print("Print bank statement")
menu=int(input("Enter 1 for student , 2 for teacher and 3 for administration"))
match menu:
    case 1:
        print("Student")
        login=int("""Enter 1 for Profile
             Profile
             Marks
             Attendence
             Courses""")
        match login:
            case 1:
                print("Profile")
            case 2:
                print("Marks")
            case 3:
                print("Attendence")
            case 4:
                print("Courses")
    
   
    case 2 :
        print("Teacher")
        login=int(input("Enter Number 1 to 4"))
  
        
    case 3:
        print("Administration")
    
