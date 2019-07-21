class rectangle:
    lst=[]
    def __init__(self):
        self.width=int(0)
        self.length=int(0)
        self.area=0
        self.perimeter=0
    def __str__(self):
        return ' this is a rectangle, the width of the recangle is %s, and the length of the rectangles is%s' % (self.width,self.length)
    def get_area(self):
        self.area=self.width*self.length
        self.perimeter=2*self.length+2*self.width
        return self.area

    def __eq__(self,other):
        if (self.width ==other.width or self.width==other.length) and (self.length==self.length or self.length==self.width):
            return True
        else:
            return False



rec=rectangle()


def get_rectangle():
    rec.length=int(input("please enter the length"))
    rec.width=int(input("please enter the width"))
    rec.get_area()
    return rec

def get_all():
    rec.lst=[]
    for a in range (2):
        rec.lst.append(get_rectangle())

get_all()
r1=rec.lst[0]
r2=rec.lst[1]
print(r1==r2)



print(get_rectangle())
