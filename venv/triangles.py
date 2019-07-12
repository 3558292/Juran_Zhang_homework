class triangle():
    def __init__(self):
        triangle_side1=0
        triangle_side2=0
        triangle_side3=0

    def read_triangle(self):
        print("please enter the length for side1:")
        self.triangle_side1=int(input())
        print("please enter the length for side2:")
        self.triangle_side2=int(input())
        print("please enter the length for side3:")
        self.triangle_side3=int(input())

    def is_triangle(self):
        if self.triangle_side1+self.triangle_side2>self.triangle_side3\
            and self.triangle_side2+self.triangle_side3>self.triangle_side1\
            and self.triangle_side1+self.triangle_side3>self.triangle_side2:
            print("the triangle is valid")
        else:
            print("the triangle is invalid")


sanjiaoxing=triangle()
sanjiaoxing.read_triangle()
sanjiaoxing.is_triangle()

