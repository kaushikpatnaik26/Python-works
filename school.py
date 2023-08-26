# create a school class a nd use multi level inhertance
class school:
    def name(self):
        print('Kendriya Vidyalaya')
class std(school):
    def std(self):
        print('12th std')
class stream(std):
    def stream(self):
        print('Science')

s = stream()
s.name()
s.std()
s.stream()