# Note taking app
# 

from AudioCapture import AudioCapture
import time

ad = AudioCapture()
ad.record()

while True:
    input()
    print(ad.getCurrentChunk())