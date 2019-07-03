print("please enter your grade")
a=int(input())
if a>100 or a<0:
    print("invalid grade")
elif a>=90 and a<=100:
    print("your grade is A")
elif a<90 and a>=80:
    print("your grade is B")
elif a<80 and a>=70:
    print("your grade is C")
elif a<70 and a>=60:
    print("your grade is D")
else:
    print("your grade is F")