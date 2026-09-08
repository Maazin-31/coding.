hour = int(input("Enter hour (0-23): "))

if not 0 <= hour <= 23:
    print("Invalid hour")
elif hour < 12:
    print("Morning")
elif hour < 17:
    print("Afternoon")
elif hour < 21:
    print("Evening")
else:
    print("Night")
