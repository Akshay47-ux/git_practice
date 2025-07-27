class vehicle:
    def __init__(self):  
        pass    
    def start(self):
        print("the vehicle has started")
    def stop(self):
        print("engine has stopped")       
class car(vehicle):
    def music(self):
        print("music playing")
def main():
    c=car()
    c.start()
    c.music()
    c.stop()
main()
#acccesing the base class methods