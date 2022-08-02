#adapter pattern in python 
from abc import abstractclassmethod


class Abstractvideo:
    @abstractclassmethod
    def __init__(self):
        pass
    @abstractclassmethod
    def sound(self):
        pass
    @abstractclassmethod
    def stop(self):
        pass

class video(Abstractvideo):    #iterface of type 1 (video)
    @classmethod
    def __init__(self):
        pass

    @classmethod
    def sound(self):
        print("Play :video")

    @classmethod
    def stop(self):
        print("stop: Video")

class Abstarctgif:
    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def play(self):
        pass
    @abstractclassmethod
    def stop(self):
        pass

class gif(Abstarctgif):  #interface of type 2 
    
    @classmethod
    def __init__(self):
        pass

    @classmethod
    def play(self):
        print("Play:gif has no sound (short video)")
    
    @classmethod
    def stop(self):
        print("stop gif")
    

"""
Now here we add an adapter to merge both the interfaces 
writing the gif adapter
"""
class gifAdapter(Abstractvideo):
    """ we pass the gif object into the constructor to map the gif to video"""
    @classmethod
    def __init__(self,gif):
        self.gif=gif
    
    @classmethod
    def sound(self):
        for i in range(5):
             self.gif.play()
    
    @classmethod
    def stop(self):
        self.gif.stop()


bwVideo=video()
bwgif=gif()
adaptedVideo=gifAdapter(bwgif)
print(adaptedVideo.play())
