hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

if hours < 0 or rate < 0:
    print("Invalid input")
elif hours > 40:
    salary = 40 * rate + (hours - 40) * rate * 1.5
    print(salary)
else:
    print(hours * rate)
