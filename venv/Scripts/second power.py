import math
print("please enter the a, b and c for the equation y=ax^2+bx+c")
print("please enter the value for a")
a=float(input())
print("please enter the value for b")
b=float(input())
print("please enter the value for c")
c=float(input())
delta=b*b-4*a*c
if(delta>0):
    print("the first root is:",float((-b+math.sqrt(delta))/2*a))
    print("the second root is:", float((-b - math.sqrt(delta)) / 2 * a))
else:
    if(delta==0):
        print("the root is:", float((-b + math.sqrt(delta)) / 2 * a))
    else:
         print("there is no root")