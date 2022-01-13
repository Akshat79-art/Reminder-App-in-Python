# An app which notifies and reminds of daily task
# Task and time can be taken from csv or excel file

import csv
import time
import sched
from win10toast import ToastNotifier

def read_from_file():  

    # Read the csv file
    
    with open('task.csv','r') as f: 
        reader = csv.DictReader(f)
        task = list(reader)
    

    # Get the time and name of task

    for i in range(len(task)):
        
        for key,value in task[i].items():               # For every dict in task
            # print(key,value)
            if key == "Time":
                time_of_task = value
            elif key == "Task":
                name_of_task = value
        tasks[time_of_task] = name_of_task              # Append time and name of task to tasks dict
    

def set_reminder():
    print(tasks)
    for key,value in tasks.items():                     # Take the key which has time and parse it appropriately
        hour = int(key[0:2])
        min = int(key[3:5])
        if (hour == time.localtime().tm_hour and min == time.localtime().tm_min):       # If it's notification time
            toast = ToastNotifier()                                                     # Create a toast
            toast.show_toast("Notification",f"{value}")                                 # Show the toast

tasks = {}
event_schedule = sched.scheduler(time.time, time.sleep)
read_from_file()                                        # Read the file and update the dict

while True:
    event_schedule.enter(60, 1, set_reminder, ())
    event_schedule.run()



## FORMAT OF CSV FILE
# Time,Task
# 20:00,Eat Food

# i.e w/o space after comma, time in 24 hr format
# Add win10toast to the directory
# As per program, task.csv is the csv file
# If you change the file name, make appropriate changes in code as well 