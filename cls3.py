class dog:
    #initiailizer
    def __init__(self, name, age, col):
        self.name = name
        self.age = age
        self.col = col
        #instance methods
    def description(self):
        return "{} is {} years old with {} color".format(self.name, self.age, self.col)
    
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    
# instantiate the dog object
name = str(input("Dog name:"))
age = int(input("Age:"))
col = str(input("Color:"))
sound= str(input("Sound:"))
s = dog(name, age, col)

# call our instance methods
print(s.description())
print(s.speak(sound))

