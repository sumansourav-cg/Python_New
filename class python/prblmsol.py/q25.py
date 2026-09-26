total=0
grade=""
for i in range(5):
    marks=int(input("Enter marks"))
total=total+marks
perc=total/5

if marks<=35:
     print("Fail")
else:
    
    if perc>=90:
          grade="A+"
    elif perc>=80:
           grade="A"
    elif perc>=70:
           grade="B"
    elif perc>=60:
           grade="C"
    else:
           grade="F"




