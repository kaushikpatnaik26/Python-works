# using multiple inheritance find sum product and division of 2 numbers
class sum:
    def add(self, a , b):
        return a+b
    
class subtraction:
    def minus(self, a, b):
        return a-b

class division:
    def div(self, a, b):
        return a/b
    
class product():
    def prod(self, a , b):
        return a*b
    
class num(sum, product, division, subtraction):
     def x(self):
         print("Enter details:")
         
a = int(input("A:"))
b = int(input("B:"))

n = num()
print(n.add(a, b))
print(n.div(a, b))
print(n.prod(a, b))
print(n.minus(a, b))

    