day = int(input("Enter day number (1-7): "))
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days[day - 1] if 1 <= day <= 7 else "Invalid day")
