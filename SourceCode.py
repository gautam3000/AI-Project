import datetime
import os
import time
import random
import webbrowser

print("==================================================================================================================")
print()
print("                                         WELCOME TO ALARM TOOL SYSTEM                                           ")
print()
print("==================================================================================================================")
print("Hello! Set a Alarm")

# If the video URL file doesn't exist, creates one
if not os.path.isfile("youtube_alarm_videos.txt"):
	print('Creating "youtube_alarm_videos.txt"...')
	with open("youtube_alarm_videos.txt", "w") as alarm_file:
		alarm_file.write("https://youtu.be/h1C-qA7BkP0")

def check_alarm_input(alarm_time):
	"""Check to see if the user has entered during a legitimate alarm time*"""
	if len(alarm_time) == 1: # [Hour] Format.
		if alarm_time[0] < 24 and alarm_time[0] >= 0:
			return True
	if len(alarm_time) == 2: # [Hour:Minute] Format.
		if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
		   alarm_time[1] < 60 and alarm_time[1] >= 0:
			return True
	return False

# Get the user input for the alarm time
print("Set a time for the alarm (Ex. 10:30)")
while True:
	alarm_input = input(">> ")
	try:
		alarm_time = [int(n) for n in alarm_input.split(":")]
		if check_alarm_input(alarm_time):
			break
		else:
			raise ValueError
	except ValueError:
		print(">> ERROR : Please Enter time in HH:MM or HH:MM:SS format only <<")

# Convert alarm time from [H:M] or [H:M:S] to seconds
seconds_hms = [3600, 60, 1] # No. of seconds in an Hour, Minute, and Second
alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

# Get this time of the day in seconds
now = datetime.datetime.now()
current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

# Calculate the number of seconds until alarm burst
time_diff_seconds = alarm_seconds - current_time_seconds


if time_diff_seconds < 0:
	time_diff_seconds += 86400 # number of seconds during on a daily basis

# Display the number of some time until the alarm burst
print("The Alarm set to travel off in %s" % datetime.timedelta(seconds=time_diff_seconds))

# Sleep until the alarm burst
time.sleep(time_diff_seconds)

# Time for the alarm to travel off
print("Wake Up! Wake Up!")

# Load list of possible video URLs
with open("youtube_alarm_videos.txt", "r") as alarm_file:
	videos = alarm_file.readlines()

# Open a random video from the list
webbrowser.open(random.choice(videos))
