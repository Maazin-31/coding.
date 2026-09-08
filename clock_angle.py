hour, minute = map(int, input("Enter hour and minute: ").split())

if not (1 <= hour <= 12 and 0 <= minute <= 59):
    print("Invalid time")
else:
    hour_angle = (hour % 12) * 30 + minute * 0.5
    minute_angle = minute * 6
    angle = abs(hour_angle - minute_angle)
    angle = min(angle, 360 - angle)
    print(angle)
