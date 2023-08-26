#create student class with attributes name, rollno, sec

class student:
    def __init__(self, name, rollno, sec):
        self.name= name
        self.rollno = rollno
        self.sec = sec
    
    def statement(self):
        return "Name: {} \nSection: {} \nRoll no: {}".format(self.name, self.sec, self.rollno)

x = student("Sai", "C", 7)

print(x.statement())
     