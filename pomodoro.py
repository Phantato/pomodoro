debug = True
#debug = False

import time
import os
currentDirectory = os.getcwd()
wavDirectory = currentDirectory + "/WAV/"
userDirectory = currentDirectory + "/User/"
endwav = wavDirectory + "time.wav"

def alart(times): os.system(("mplayer " + endwav +  "< /dev/null > /dev/null 2>1;") * times)

with open(userDirectory + "user.bin", "br") as userFile:
    userPomodoroTimes = int.from_bytes(userFile.read(4), "big")
print(userPomodoroTimes)

setPomodoroTimes = int(input("How many pomodoro would you start?:"))
passedPomodoroTimes = 0
print("Starting Pomodoro!")


startTime = int(time.time())
print("Start at " + time.strftime("%H:%M:%S"))
restFlag = True
print("")

while setPomodoroTimes > passedPomodoroTimes:
    currentTime = int(time.time())
    if restFlag and ((currentTime - startTime) >= 1500 or (debug and currentTime - startTime >= 10)):
        alart(3)
        print("It's time to take a break!")
        restFlag = False
        startTime = int(time.time())
        print("Start at " + time.strftime("%H:%M:%S"))
        passedPomodoroTimes += 1
        userPomodoroTimes += 1
    elif not restFlag and ((currentTime - startTime) >= 300 or (debug and currentTime - startTime >= 3)):
        alart(3)
        print("It's time to work!")
        restFlag = True
        startTime = int(time.time())
        print("Start at " + time.strftime("%H:%M:%S"))
with open(userDirectory + "user.bin", "bw") as userFile:
    userFile.write(userPomodoroTimes.to_bytes(4, "big"))
