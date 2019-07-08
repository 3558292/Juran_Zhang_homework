#this function is to add two lists of numbers together then multiply the numbers by a constant
def sum_list(a,b):
    lstC=[]
    i=1
    z=0
    if len(a)<=len(b):
        for i in range(0,len(b)-len(a)):
            a.append(0)
            i+=1
        for z in range (0,len(b)):
            q=a[z]+b[z]
            lstC.append(q)
        del lstC[0]
        print(lstC)
    else:
        for i in range(1,len(a)-len(b)):
            b.append(0)
            i+=1
        for z in range(0,len(a)):
            q = a[z] + b[z]
            lstC.append(q)
        print(lstC)
    del lstC[0]
    return lstC

def mul_list(c,lst):
    lstD=[]
    for k in range(len(lst)):
        lst[k]=lst[k]*c
        lstD.append(lst[k])
    print(lstD)
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

sum_list(lstA,lstB)
list=sum_list(lstA,lstB)
mul_list(3,list)

