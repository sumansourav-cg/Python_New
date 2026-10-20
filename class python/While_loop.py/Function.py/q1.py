# def welcome():
#     print("Welcome To Python")

# welcome()

# Q2

# def greet(name):
#     return name
# print(greet("Suman"))

# Q3
# def show_number(number):
#     return number
# print(show_number(99))

# Q4

# def add(a,b):
#     return a+b
# print(add(23,45))

# Q5
# def square(number):
#     return number*number
# print(square(22))

# Q6  
# def is_even(number):
#     if number%2==0:
#         return "True"
#     else:
#         return "Falsee"
# print(is_even(33))

# Q7
# def get_full_name(name):
#    string=name.split()
#    First_name=string[0]
#    Last_name=string[1]
#    return f"{First_name},{Last_name}"
# print(get_full_name("Suman Sourav"))

# Q8
# def introduce(name,city="Pune"):
#     return city,name
# print(introduce("Suman"))

# Q9
# def subtract(a,b):
#  return a-b
# print(subtract(33,11))

# Q10
# def get_min_max(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(get_min_max(22,55))


# Q11
# i=int(input("Enter number between 1 to 4"))
# def calculate(a,b):
#     if i==1 and b!=0:
#         return a+b
#     elif i==2 and b!=0:
#         return a-b
#     elif i==3 and b!=0:
#         return a/b
#     elif i==4 and b!=0:
#         return a//b
#     else:
#         print("Enter valid value")

# print(calculate(33,11))

# Q12
# def count_digit(number):
#     if number>=0:
#         number=str(number)
#         length=len(number)
#         return length
# print(count_digit(22))

# Q13
# def classify_number(number):
#     if number>0:
#         return "Positive"
#     elif number<0:
#         return "Negative"
#     else:
#         return "Zero"

# Q14
# def calculate_price(price,quantity=8):
#     return price*quantity
# print(calculate_price(22))

# Q15
# def create_email(username,domain="example.com"):
#     return username+domain
# print(create_email("Suman"))

# Q17
# def percentage(marks,total=100):
#     return marks/total*100
# print(percentage(99))


# q18
# def convert_minutes(minutes,second_per_minutes):
#     return minutes*60+second_per_minutes
# print(convert_minutes(5,10))
# q19
# def student_details(name,age,city):
#     return name,age,city
# print(student_details(name="Suman",age=22,city="Bokaro"))


# Q20
# def bill(item,quantity=1,price=100):
#     return price*quantity
# print(bill(item=1,quantity=2,price=500))


# Q21
# def analyze_number(number):
#     if number%2==0:
#         print("Even")
#         number=str(number)
#         length=len(number)
#         return length

#     elif number<0:
#         return number*(-1)
   
       
# print(analyze_number(32))   




# def calculate_stats(a,b,c):
#     if a>b and a>c:
#         print("A is the greatest")
#     elif b>a and b>c:
#         print("B is the Greatest")
#     else:
#         print("C is the greatest")
# print(calculate_stats(33,44,55))

# Q23

# def make_sentence(subject,verb,object):
#     return subject+verb+object
# print(make_sentence())

# Q24

# def calculate_pay(hours,rate=200,bonus=0):
#     return hours*rate+bonus
# print(calculate_pay(12))

# Q25
# def get_coordinate(x=0,y=0):
#     return x,y
# print(get_coordinate(x=20,y=30))

# def compare(a,b):
#     if a>b:
#         return a
#     else:
#         return b

# print(compare(22,44))

# Q27

# def calculate_result(marks,passing_marks=35):
#     if marks>passing_marks:
#         return "Pass"
#     else:
#         return "Fail"
# print(calculate_result(44))


# Q28

# def order_summary(items,quantity=1,price=100,delivery_fee=40):
#     return quantity*price+delivery_fee
# print(order_summary(delivery_fee=30,price=7,quantity=4,items=3))

