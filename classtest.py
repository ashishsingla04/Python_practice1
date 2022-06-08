class computer :
    def __init__(self):
        self.name='Navin'
        self.age=28
    def update(self):
        self.age=40
        self.name='Satish'

c1=computer()
c2=computer()

c1.name='Ashish'
c1.age=30


print(c1.name,c1.age)
c2.update()
print(c2.name,c2.age)