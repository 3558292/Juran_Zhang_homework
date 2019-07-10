def st(x):
    for i in range(len(x)):
        for j in range(len(x)-1-i):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
    return x


def input_player():
    jersey_player={}
    jersey_number = int(input("please enter the number of the player"))
    jersey_rating = int(input("please enter the rating of the player"))
    lst=[]
    while 0 < jersey_rating <10 and 0 <= jersey_number <100:
        jersey_player[jersey_number] = jersey_rating
        jersey_number =int( input("please enter the number of the player"))
        jersey_rating = int(input("please enter the rating of the player"))
    else:
        print("you have now input a number out of range, the loop now break")
    print(jersey_player)
    for i in jersey_player:
        lst.append(i)
    st(lst)
    for b in lst:
        print("the player with the number of",b,"'s rating number is",jersey_player[b])


input_player()