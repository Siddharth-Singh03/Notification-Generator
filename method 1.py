import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title = "All day reminder",
            message =  "submit your mini project",
            timeout = 15
        )
        time.sleep(3)

