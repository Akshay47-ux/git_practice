class Mediaplayer:
    def paly(self):
        return "over riding this  to  demonstrate run timr polymorphism"
    def info(self):
        return "this too "
    
class MP3(Mediaplayer):
    def play(self):
        return "plying music"
    def info(self):
        return "using MP3 player"

class MP4(Mediaplayer):
    def play(sself):
        return "playing video "
    def info(self):
        return "using something which works with video  "
class Avi(Mediaplayer):
    def play(self):
        return "playing avi file"
    def info(self):
        return "using avi decoder"
class Flac(Mediaplayer):
    def play(self):
        return "playing flac file"
    def info(self):
        return "i dont know what this uses"
def main():
    m=MP3()
    m1=MP4()
    a=Avi()
    f=Flac()
    file=[m,m1,a,f]
    for x in file:
        print(x.play(),x.info())
main()
