# MULTIPLE INHERITANCE

class BMW:
    def show(self):
        print("BMW is a car")

class Merc:
    def show(self):
        print("Merc is a car")

class Car(BMW, Merc):
    def show(self):
        print("Both are cars")

c= Car()
b= BMW()
m = Merc()

b.show()
m.show()
c.show()
