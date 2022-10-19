# alarm.py

# define variables
current_time = input("what is the current time?")
alarm_time = input("How many hours to wait for the alarm?")
current_time = int(current_time)
alarm_time = int(alarm_time)
# calculate
wakeup_time = (current_time + alarm_time) % 24
# output
print("The alarm will wake you up at",wakeup_time)
