class Files:
    def play(self):
        return "we're gonnna over ride this method"
    
class Mp3(Files):
    def play(self):
        return "playing mp3 file"

class Mp4(Files):
    def play(self):
        return "playing mp4 file"

def main():
    m=Mp3()
    m1=Mp4()
    file=[m,m1]
    for i in file:
        print(i.play())
main()
