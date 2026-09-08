month = int(input("Enter month number (1-12): "))
year = int(input("Enter year: "))

if month == 2:
    days = 29 if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else 28
elif month in (4, 6, 9, 11):
    days = 30 if 1 <= month <= 12 else None
elif 1 <= month <= 12:
    days = 31
else:
    days = None

print(days if days is not None else "Invalid month")
