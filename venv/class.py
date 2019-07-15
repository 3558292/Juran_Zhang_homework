class student:
    def __init__(self):
        self.name=""
        self.age=int(0)
        self.grade_list=[]
        self.GPA=int(0)
        self.gra_day=0
        self.gra_month=0
        self.gra_year=0

    def read_from_keyboard(self):
        x=0
        self.name=input("please enter the student's name")
        self.age=input("pease enter the student's age")
        self.gra_day = input("pease enter the student's graduation day")
        self.gra_month = input("pease enter the student's graduation month")
        self.gra_year = input("pease enter the student's graduation year")
        print("pease enter numbers fot the student's grade")
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
        print("graduation day",self.gra_day)
        print("graduation month", self.gra_month)
        print("graduation year", self.gra_year)
        print("grade list",self.grade_list)
        print("GPA is",self.GPA)


study=student()
study.read_from_keyboard()
study.find_GPA()
study.print_student()