class A:
    def __init__(self):
        x=12
        y=23
class B(A):
    def __init__(self):
        self.x=2
        self.y=43
def main():
    b=B()
    print(b.x,b.y)              
main()    
#this program demonstrates that the init function in th derived class will ovrride
# the one in the basse clas  