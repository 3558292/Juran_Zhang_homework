def check():
    x=0
    lst=[]
    print("please enter a set of number")
    while x>=0:
        x=int(input())
        lst.append(x)
    print("please enter a number")
    y=int(input())
    for i in range(0,len(lst)):
        if lst[i]!=y:
            i=i+1
        else:
            if lst[i]==y:
                print("the number exist, and the index of this is",i)
            break
    else:
        print("the number dose not exist")


check()