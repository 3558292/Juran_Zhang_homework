print("please enter two number")
b=int(input())
s=int(input())

while s!=0:
    i=b%s
    b=s
    s=i
print(b)
