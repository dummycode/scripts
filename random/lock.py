from datetime import datetime, time
import subprocess

def is_between(current_time, start, end):
    return current_time > start and current_time < end

def is_weekday(current_time):
    return current_time.weekday() < 5

current_datetime = datetime.now()
current_time = current_datetime.time()

morning, evening = time(8, 0), time(17, 0)
if is_weekday(current_datetime) and is_between(current_time, morning, evening):
    response = input("Have you set your status in Slack? [y/n]\n")
    if response != "y":
        print("Do that!")
        exit()

print("Locking...")
subprocess.run('osascript lock.scpt'.split(' '))

