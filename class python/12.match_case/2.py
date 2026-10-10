# a=int(input("Enter a : "))
# b=int(input("Enter b : "))
# # oparation=input("Menu : \n+ Addtion\n- substraction\n* multiplication\n/ division\n% modulus\n//floor-division \nEnter your choice : ")

# # match oparation:
# #     case "+":
# #         print("Addition ",a+b)
# #     case "-":
# #         print("Substraction : ",a-b)
# #     case "*":
# #         print("multiplication : ",a*b)
# #     case "/":
# #         print("division : ",a/b)
# #     case "%":
# #         print("modulus : ",a%b)
# #     case "//":
# #         print("modulus : ",a//b)
# #     case _:
# #         print("invalid")

# # # choice=int(input("Menu : \n1. Addtion\n2. substraction\n3. multiplication\n4.Exist"))
# # choice=int(input("Menu : \n1. Addtion\n2. substraction\n3. multiplication\n4.Exist\nEnter your choice : "))

# # while choice!=4:

# #     match choice:
# #         case 1:
# #             print("addition : ",a+b)
# #         case 2:
# #             print("sub : ",a-b)
# #         case 3:
# #             print("multiplication : ",a*b)
# #         case 4:
# #             break
# #         case _:
# #             print("invalid choice ")
# #     choice=int(input("Menu : \n1. Addtion\n2. substraction\n3. multiplication\n4.Exist"))


# num=int(input("Enter a number : "))

# operation=int(input("Menu : \n1.Even\n2.Odd\n3.Prime \nEnter your choice : "))
# match operation:
#     case 1:
#         if num%2==0:
#             print("Even number")
#         else:
#             print("not an even number")
#     case 2:
#         if num%2==1:
#             print("odd number")
#         else:
#             print("not an odd number")
#     case 3:
#         for i in range(2,num):
#             if num%i==0:
#                 print("not prime ")
#                 break
#             else:
#                 print("prime")
#                 break
# #------guard (bakvash hai not imp at all)------------
# marks=float(input("Enter marks : "))

# match marks:
#     case x if x>=90:
#         print("A")
#     case x if x>=75:
#         print("B")
#     case x if x>=60:
#         print("C")    
#     case x if x>=30:
#         print("D")
#     case _:
#         print("fail")

category=int(input("1.Gase\n2.Electricity\nEnter your choice"))
type=int(input("ENter type : "))
match category:
    case 1:
        
        match type:
            case 1:
                print("Residential Gas Plan") 
            case 2:
                print("commercialtial Gas Plan") 
            case 3:
                print("industrial Gas Plan")    
    case 2:
        match type:
            case 1:
                print(" Electricity Domestic Prepaid") 
            case 2:
                print("Electricity Domestic Postpaid") 
            case 3:
                print("Electricity Agricultural Tariff")                
            