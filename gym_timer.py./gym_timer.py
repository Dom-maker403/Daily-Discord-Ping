import datetime

# Your gym time is 11:30 AM (11.5)
gym_time = 11.5
now = datetime.datetime.now()
current_hour = now.hour + (now.minute / 60)

if current_hour < gym_time:
    diff = round(gym_time -
current_hour, 1)
    print(f"You have {diff} hours left before the gym.")
else:
    print("Time to head out!")