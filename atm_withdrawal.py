balance = float(input("Enter balance: "))
amount = float(input("Enter withdrawal amount: "))
minimum_balance = float(input("Enter required minimum balance: "))

if amount <= 0:
    print("Invalid withdrawal amount")
elif amount > balance:
    print("Insufficient balance")
elif balance - amount < minimum_balance:
    print("Withdrawal rejected: minimum balance rule")
else:
    balance -= amount
    print("Withdrawal approved")
    print("Remaining balance:", balance)
