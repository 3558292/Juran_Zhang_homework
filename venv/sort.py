def st(x):
    for i in range(len(x)):
        for j in range(len(x)-1-i):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
    return x
lst=[12,23,34,1,45,-3,12]

print(st(lst))

