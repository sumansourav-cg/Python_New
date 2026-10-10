# day=int(input("Enter day : "))
# match day:
#     case 1 | 2 | 3 |4| 5:
#         print("weekday")
#     case 6|7:
#         print("weekend")
#     case _:
#         print("invalid ")

account = int(input("Enter account type: "))

match account:
    case 1:
        print("Savings Account")
    case 2:
        print("Current Account")
    case _:
        print("Invalid Account Type")

amount = float(input("Enter amount: "))

if amount > 0:
    print("Withdrawal Request Accepted")
else:
    print("Invalid Amount")

