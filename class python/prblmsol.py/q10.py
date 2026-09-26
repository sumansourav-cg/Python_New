a=int(input("Enter a number "))
if a<0 :
    print("Inavalid age")
elif a>=18 and a<120:
    print("Can Vote")
elif a<18:
    print("Cannot vote")
else:
    print("Unrealistic age")