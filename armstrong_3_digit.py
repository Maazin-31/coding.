n = int(input("Enter a 3-digit number: "))

if 100 <= n <= 999:
    digits = [int(d) for d in str(n)]
    print("Armstrong number" if sum(d ** 3 for d in digits) == n else "Not an Armstrong number")
else:
    print("Please enter a 3-digit number")
