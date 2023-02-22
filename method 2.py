#importing necessary libraries

import time, datetime
from win10toast import ToastNotifier

#method to define current time
def timeinfo():
	hours = int(input("enter the hours of interval :"))
	minutes = int(input("enter the minutes of  interval :"))
	seconds = int(input("enter the seconds of intereval :"))
	time_interval = seconds+(minutes*60)+(hours*3600)
	return time_interval

def note():
	now = datetime.datetime.now()
	starttime = now.strftime("%H:%M:%S")
	
	#creating a "log" file that will save the message that was displayed and at what time it was displayed. 
	
	with open("log.txt", 'a') as f:
		f.write(f"you drank water at {now} \n")
	return 0

#method to display the message in the notification
def notify():
	Notification = ToastNotifier()
	Notification.show_toast("time to drink water")
	note()
	return 0

#setting up the time interval
def starttime(time_interval):
	while True:
		time.sleep(time_interval)
		notify()


if __name__ == '__main__':
	time_interval = timeinfo()
	starttime(time_interval)

