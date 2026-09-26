a=int(input("Enter amount "))
if 0<a<500:
    print(a)
elif 500<a<=1000:
        print(a-a*0.05)
elif 1000<a<1999:
           print(a-a*0.1)
elif 2000<a<4999:
   print(a-a*0.15)
elif a>=5000:
 print(a-a*0.2)
else:
 print("Invalid")
 
        
     