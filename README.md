## Notification Generator

A notification generator is a tool or program that creates and sends notifications to users on different platforms or devices. These notifications can be in the form of pop-ups, sounds, messages, or alerts that provide information, updates, or reminders about specific events or activities.


## Libraries used
1. time - https://docs.python.org/3/library/time.html

2. plyer - It is a Python library for accessing features of your hardware / platforms.

3. datetime - https://docs.python.org/3/library/datetime.html

4. win10toast - python library for displaying desktop notifications.


## Method-1
1. It's a short method to generate notification
2. It only displays the notification with the message provided in the given timeperiod
3. The title, message and time period has to be given in the code itself.


## Method-2
1. This is a much organised way to display notifications
2. generating notifications, message to be showed and time interval are all defined in a separate functions.
3. Saves the message and time when the notification was displayed in a separate file as database.
