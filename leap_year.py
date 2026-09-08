year = int(input("Enter year: "))
print("Leap year" if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else "Not a leap year")
