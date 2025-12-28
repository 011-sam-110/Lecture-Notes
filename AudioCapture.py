import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel
import datetime


sd.default.device = (8, 1)

class AudioCapture:
    chunkNo = 1

    def __init__(self, duration=15, samplerate=44100):
        self.__duration = duration
        self.__samplerate = samplerate
        
    def record(self):
        
        myrecording = sd.rec(int(self.__duration * self.__samplerate), 
            samplerate=self.__samplerate, channels=2, dtype="float64")
        
        sd.wait()  # wait for recording to finish

        filename = f"Chunk {self.chunkNo}.wav"
        write(filename, self.__samplerate, myrecording)
        self.chunkNo += 1
    
    def getCurrentChunk(self):
        return self.chunkNo





audio = AudioCapture()
audio.record()




#Where are we?
#everything works, and tts is functioning. 
#need to impliment chunking, 30 second splits between recording, before its passed into tts
#from tts, need to introduce another AI model with instructions on how to format notes
# As an extra, it may also try to include more information/fill knowledge gaps