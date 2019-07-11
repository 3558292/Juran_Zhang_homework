def output_menu():
    print("please choose a character, remember to write them uncapitalized")
    print("A-Add players")
    print("D-Remove players")
    print("U-update player rating")
    print("R-Output players above a rating")
    print("O-Output roster")
    print("Q-Quit")


def st(x):
    for i in range(len(x)):
        for j in range(len(x)-1-i):
            if x[j]>x[j+1]:
                x[j],x[j+1]=x[j+1],x[j]
    return x

def input_player(jersey_player):
    jersey_number = int(input("please enter the number of the player"))
    jersey_rating = int(input("please enter the rating of the player"))
    lst=[]
    while 0 < jersey_rating <10 and 0 <= jersey_number <100:
        jersey_player[jersey_number] = jersey_rating
        jersey_number =int( input("please enter the number of the player"))
        jersey_rating = int(input("please enter the rating of the player"))
    else:
        print("you have now input a number out of range, the loop now break")
    for i in jersey_player:
        lst.append(i)
    st(lst)
    for b in lst:
        print(b,":",jersey_player[b])
    return jersey_player


def add_player(x):
    print("please add the player's number and rating")
    a=int(input("please enter the player's jersey number and his rating number"))
    b=int(input("please enter the player's rating number"))
    while 0 < b <10 and 0 <= a <100:
        x[eval(a)] =eval(b)
    else:
        print("you have now input a number out of range, the loop now break, please try again")
    print(x)


def update_player(x):
    print("please enter the player's number that you want to change, and then enter the new rating number")
    a=int(input("please enter the player's jersey number"))
    if a in x:
        print("please enter the new rating number")
        b=int(input())
        if 0<b<10:
            x[eval(a)]=eval(b)
            print(x)
        else:
            print("you have enter a number that is out of range, please try again")
    else:
        print("the number you entered is not in the roster,please try again")







def delete_player(a):
    print("please enter the the player that you want to delete")
    x=input()
    if eval(x) in a:
        del a[eval(x)]
        print (a)
    else:
        print("you have enter a number that is not in the roster")

dictionary={}
input_player(dictionary)
output_menu()
print("now please choose a character, remember to write them uncapitalized")
x=str(input())
if x=="a":
        print("now please enter the players' jersey number and their rating number")
        add_player(dictionary)
elif x=="d":
        delete_player(dictionary)
elif x=="r":
    delete_player(dictionary)
elif x=="o":
    print(dictionary)
elif x=="q":
    print("you now quit the program")
elif x=="u":
    update_player(dictionary)
else:
    print("you have enter a number that is not on the menu, please try again")




