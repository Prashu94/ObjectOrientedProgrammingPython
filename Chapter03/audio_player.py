import abc


class AudioFile:

    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")

        self.filename = filename


class MP3File(AudioFile):
    ext = "mp3"

    def play(self):
        print("playing {} as mp3".format(self.filename))


class WavFile(AudioFile):
    ext = "wav"

    def play(self):
        print("playing {} as wav".format(self.filename))


class OggFile(AudioFile):
    ext = "ogg"

    def play(self):
        print("playing {} as ogg".format(self.filename))


class FlacFile(AudioFile):
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("Invalid File Format")
        self.filename = filename

    def play(self):
        print("playing {} as flac".format(self.filename))


class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass

    @property
    @abc.abstractmethod
    def ext(self):
        pass

    @classmethod
    def __subclasshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented


if __name__ == "__main__":
    """
    1. The OggFile constructor calls the constructor in AudioFile
    with the filename.
    2. The ogg object will call its play method .
    """
    ogg = OggFile("myfile.ogt")
    # Override call to the ogg file.
    print(ogg.play())
"""abc module means AbstractBaseClass 
1. class abc.ABC : helper class that has ABCMeta as its metaclass.
- With this an abstract base class can be derived from ABC.
2. class abc.ABCMeta
- Metaclass for defining AbstractBaseClasses.
- has the following methods.
a. register(subclass) - register subclass as a "virtual subclass" of ABC.
3. @abc.abstractmethod
- a decorator indicating an abstract methods.
- using this decorator requires that the class's metaclass is ABCMeta
or is derived from it.
4. @classmethod - Convert the function to class method.

"""
