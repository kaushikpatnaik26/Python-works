# MULTI LEVEL INHERITANCE

class vegetable:
    def show(self):
        print("Green Veggie")

class spinach(vegetable):
    def show(self):
        super().show()
        print("Leafy Veggie")

class carrot(spinach):
    def show(self):
        super().show()
        print("Orange Veggie")

c = carrot()
s = spinach()
v = vegetable()
c.show()
s.show()
v.show()
