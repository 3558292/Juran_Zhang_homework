class student:
    lst=[]
    def __init__(self):
        self.name=""
        self.age=int(0)
        self.grade_list=[]
        self.GPA=int(0)
        self.gra_day=0
        self.gra_month=0
        self.gra_year=0

    def __str__(self,other):
        return '%02d student name is %s, his/her age is %02d, and the GPA is' % (self.name,self.age,self.GPA)

    def __eq__(self,other):
        if self.name ==other.name:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.GPA<other.GPA:
            return True
        else:
            return False

    def __gt__(self,other):
        if self.GPA >other.GPA:
            return True
        else:
            return False

    def read_from_keyboard(self):
        x=0
        self.name=input("please enter the student's name")
        self.age=int(input("pease enter the student's age"))
        while self.age<=0:
            print("invalid number, please try again")
            self.age=int(input())
        self.gra_day = int(input("pease enter the student's graduation day"))
        while self.gra_day<=0 or self.gra_day>31:
            print("invalid number, please try again")
            self.gra_day=int(input())
        self.gra_month = int(input("please enter the student's graduation month"))
        while self.gra_month<=0 or self.gra_month>12:
            print("invalid number, please try again")
            self.gra_month=int(input())
        self.gra_year = int(input("please enter the student's graduation year"))
        print("please enter numbers fot the student's grade")
        while x>=0:
            x=int(input())
            self.grade_list.append(x)
        else:
            print("you have just input a number that is out of range, the loop break")

    def find_GPA(self):
        y=0
        i=0
        for i in range (0,len(self.grade_list)-1):
            y+=self.grade_list[i]
        print("the total grade for this student is:",y)
        self.GPA=y/(i+1)
        print("the student's GPA is:",self.GPA)

    def print_student(self):
        print("student's name:",self.name)
        print("student's age:",self.age)
        print("graduation day:",self.gra_day)
        print("graduation month:", self.gra_month)
        if self.gra_year<0:
            print("graduation year:", self.gra_year*-1,"B.C.")
        else:
            print("graduation year:",self.gra_year,"A.D.")
        del self.grade_list[len(self.grade_list)-1]
        print("grade list",self.grade_list)
        print("GPA is",self.GPA)


def get_all():
    student.lst=[]
    for a in range (2):
        s1=student()
        s1.read_from_keyboard()
        s1.find_GPA()
        student.lst.append(s1)


get_all()
for i in student.lst:
    i.print_student()



