



#Type of positional arguement

#.1

class Parent:
    def __init__(self, a, b):
        self.p = a
        self.q = b

    def google(self):
        print("google")

    def apple(self):
        print("1st :", self.p, "2nd :", self.q)
        self().google()

x = Parent(1,2)
x.apple()

#1.1 seperate method


#1.2 override the existing method in parent class

class Child1(Parent):
    def apple(self):
        print("child 1")
        self().google()
    #def apple(self)"

y = Child1(4,5)
y.apple()
y.google()
x.google()
#1.2 override







