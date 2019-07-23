class my_long_int:
    def __init__(self, str1):
        self.lst =[]
        self.str=str1
    def __add__(self, other):
        if int(self.str) < 0 and int(other.str) < 0:
            self.str = str(abs(int(self.str)))
            other.str = str(abs(int(other.str)))
            return -(self+other)
        elif int(self.str) < 0 <= int(other.str):
            self.str = str(abs(int(self.str)))
            other.str = str(abs(int(other.str)))
            return (other - self)
        elif int(self.str) >= 0 > int(other.str):
            self.str = str(abs(int(self.str)))
            other.str = str(abs(int(other.str)))
            return self - other
        for i in self.str:
            self.lst.append(i)
        for i in other.str:
            other.lst.append(i)
        lst=[]
        if len(self.lst) <= len(other.lst):
            for i in range(len(other.lst) - len(self.lst)):
                lst.append(0)
            for a in self.lst:
                lst.append(a)
            self.lst = lst
        else:
            for i in range(len(self.lst) - len(other.lst)):
                lst.append(0)
            for a in other.lst:
                lst.append(a)
            other.lst = lst
        x = self.lst
        y = other.lst
        print(x,y)
        lst_result = []
        b = len(x)-1
        q=0
        for a in range(len(x)):
            #print(x[b], y[b])
            if int(x[b]) + int(y[b]) + q < 10:
                lst_result.append(int(x[b]) + int(y[b]) + q)
                q = 0
            else:
                lst_result.append(int(x[b]) + int(y[b]) - 10 + q)
                q = 1
            b=b-1
        if int(x[b+1]) + int(y[b+1]) - 10 + q>=0:
            lst_result.append(1)
        lst_result.reverse()
        uuu=[str(i) for i in lst_result]
        #return (self.lst,other.lst)
        return int("".join(uuu))

    def __sub__(self,other):
        if int(self.str) < 0 and int(other.str) < 0:
            self.str = str(abs(int(self.str)))
            other.str = str(abs(int(other.str)))
            return (other-self)
        elif int(self.str) < 0 <= int(other.str):
            self.str = str(abs(int(self.str)))
            other.str = str(abs(int(other.str)))
            return -(other + self)
        elif int(self.str) >= 0 > int(other.str):
            self.str = str(abs(int(self.str)))
            other.str = str(abs(int(other.str)))
            return other + self
        elif int(self.str)<int(other.str):
            self.str = str(abs(int(self.str)))
            other.str = str(abs(int(other.str)))
            return -(other-self)

        for i in self.str:
            self.lst.append(i)
        for i in other.str:
            other.lst.append(i)
        lst=[]
        if len(self.lst) <= len(other.lst):
            for i in range(len(other.lst) - len(self.lst)):
                lst.append(0)
            for a in self.lst:
                lst.append(a)
            self.lst = lst
        else:
            for i in range(len(self.lst) - len(other.lst)):
                lst.append(0)
            for a in other.lst:
                lst.append(a)
            other.lst = lst
        x=self.lst
        y=other.lst
        print(x,y)
        lst_result=[]
        q=0
        b=len(x)-1
        for a in range(len(x)):
            if int(x[b])+q-int(y[b])>=0:
                lst_result.append(int(x[b])+q-int(y[b]))
                q=0
            else:
                lst_result.append(int(x[b])+10+q-int(y[b]))
                q=-1
            b=b-1
        lst_result.reverse()
        uuu = [str(i) for i in lst_result]
        # return (self.lst,other.lst)
        return int("".join(uuu))

c1 = my_long_int("-90")
c2 = my_long_int("70")
print(c1-c2)
