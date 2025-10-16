# Alarm-clock
import time
from datetime import datetime

#take user input(time)
alarm = input("set an alarm: ")

#convert it to a comparable format
currentTime = datetime.now().strftime("%H:%M:%S") #<--converting time now to a readable format
alarmTime = datetime.strptime(alarm, "%H:%M:%S").time() #<--converting str to time object

#loop through the current time(check) if currentime == user input 
while True:
    if currentTime != alarmTime:
        print("wake uppppp")
    else:
        continue






