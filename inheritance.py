# 2 classes : 1.base class/parent class
            # 2.Derived class/ child class
            
# types: 
    #    single inheritance
    #    multi level inheritance
    #    multiple inhertance
    #    hierarchial inheritance


# single inhertance:

class animal:#parent class
    def speak(self):
        print('animal speaking')
        
class dog(animal):#child class
    def bark(self):
        print('dog barking')

d = dog()
d.bark()
d.speak()


