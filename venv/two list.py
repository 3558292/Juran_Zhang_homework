#this function is to add two lists of numbers together then multiply the numbers by a constant
def sum_list(a,b):
    lstC=[]
    i=1
    z=0
    if len(a)<=len(b):
        for i in range(len(b)-len(a)):
            a.append(0)
        for z in range(len(b)):
            q=a[z]+b[z]
            lstC.append(q)
        del lstC[0]
        print("the result of this addition is:",lstC)
    else:
        for i in range(len(a)-len(b)):
            b.append(0)
        for z in range(len(a)):
            q = a[z] + b[z]
            lstC.append(q)
        del lstC[0]
        print("the result of this addition",lstC)
    return lstC

def mul_list(lst):
    print("please enter a number as the multiplier:")
    c=int(input())
    lstD=[]
    for k in range(0,len(lst)):
        lst[k]=lst[k]*c
        lstD.append(lst[k])
    print("the result of the calculation is:",lstD)
    return lstD


x="0"
y="0"
lstA=[]
lstB=[]
print("please enter a set of number for list A")
while x.isdigit():
    lstA.append(eval(x))
    x=input()
else:
    print("you have enter a character, the loop now break")
print("please enter another set of numbers for list B")
while y.isdigit():
    lstB.append(eval(y))
    y=input()
else:
    print("you have enter a character, the loop now break")
mul_list(sum_list(lstA,lstB))

