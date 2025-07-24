class A:
    def __init__(self):
        self.x = 20
        self.y = 1

class B(A):
    def __init__(self):
        super().__init__()  
        print(self.x,self.y)
        self.dis()

    def dis(self):
        self.x = 12
        self.y = 34

def main():
    obj = B()        
    print(obj.x, obj.y)
main()
