# def double(number):
#     return number*2
# def add_five(number):
#     return number+5
# result=add_five(double(2))
def counter_fun(count):
    count=count+1

    if(count==20):
        return count
    counter_fun(count)
print(counter_fun(1))


