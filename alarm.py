from cgitb import text
import tkinter
import datetime
import time
from typing import Text
import winsound

from arrow import now


def alarm (set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%D:%M:%Y")
        print("Set Date: ", date)
        print(now)


        if now == set_alarm_timer:
            print("WAKE UP!!!")
        else:
            print('dfjdsfkjsdh')
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        break

# alarm("18:36:00")

def actual_time():
    hour = set_alarm_timer = f"{hour.get()}:{mins.get()}:{sec.get()}"
    alarm(set_alarm_timer)


clock = Tk()

clock.title("Alarm Clock")
clock.geometry("400*200")
time_format = Label(clock, text="Enter time in 24 hours format!", fg="red", bg="black", font="Arial").place(x=60, y=120)
addTime = Label(clock, text= "Hour  Minutes Seconds", font=60).place(x=110)
setYourAlarm = Label(clock, text= "When to wake you up", fg="blue", relief="solid", font= ("Helevetica",7,"bold")).place(x=0, y=29)

#required variables
hour = StringVar()
mins = StringVar()
sec = StringVar()

#time required to set alarm
