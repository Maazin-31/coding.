n = int(input("Enter a number: "))

if n > 0:
    print("Positive")
    print("Even" if n % 2 == 0 else "Odd")
elif n < 0:
    print("Negative")
else:
    print("Zero")
