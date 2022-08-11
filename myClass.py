class main():
    def __init__(self):
        self.data = []
    def add(self,x):
        self.data.append(x)
    def remove(self,x):
        self.data.remove(x)

class alt(main):
    msg = 'ahoj'
    def __init__(self):
        super().__init__()
        self.add(self)
    def callit(self):
        print(self.msg)
    def add(self,x):
        super().add(x)
        self.msg = 'speci'

m = main()
s = alt()

s.callit()
print(s.data)
print(m.data)
s.callit()