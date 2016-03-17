import time
import os
currentDirectory = os.getcwd()
wavDirectory = currentDirectory + "/WAV/"
endwav = wavDirectory + "time.wav"

def alart(times): os.system(("mplayer " + endwav +  "< /dev/null > /dev/null 2>1;") * times)

startTime = int(time.time())
flag = True
while 1:
    currentTime = int(time.time())
    if flag and (currentTime - startTime) >= 1500:
        alart(3)
        print("It's time to take a break!")
        flag = False
        startTime = int(time.time())
    elif not flag and (currentTime - startTime) >= 300:
        alart(3)
        print("It's time to work!")
        flag = True
        startTime = int(time.time())
