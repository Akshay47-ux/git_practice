class person:
    def __init__(self):
        self.name="prashanth"
        self.age=17
    def show(self):
           print(self.name,self.age)    
class student(person):
    def __init__(self):
        super().__init__()
        self.marks=80
def main():
    s=student()
    s.show()
    print(s.marks,s.age)

main()
 #so here we arre demonstarting that how we can acces the base class elements in the child class            