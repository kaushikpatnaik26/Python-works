class student:
    def getdata(self):
        print('accepting data')
        self.name = input("Enter name:")
        self.contact=input("Enter contact:")

    def putdata(self):
        print("the name is:",self.name, "\nThis is the contact no:",self.contact)

a = student()
a.getdata()
a.putdata()
