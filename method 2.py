import time, datetime
from win10toast import ToastNotifier


def timeinfo():
	hours = int(input("enter the hours of interval :"))
	minutes = int(input("enter the minutes of  interval :"))
	seconds = int(input("enter the seconds of intereval :"))
	time_interval = seconds+(minutes*60)+(hours*3600)
	return time_interval


def note():
	now = datetime.datetime.now()
	starttime = now.strftime("%H:%M:%S")
	with open("log.txt", 'a') as f:
		f.write(f"you drank water at {now} \n")
	return 0


def notify():
	Notification = ToastNotifier()
	Notification.show_toast("time to drink water")
	note()
	return 0


def starttime(time_interval):
	while True:
		time.sleep(time_interval)
		notify()


if __name__ == '__main__':
	time_interval = timeinfo()
	starttime(time_interval)

