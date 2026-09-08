age = int(input("Enter age: "))

# Example pricing rule; adjust these amounts if your class specifies different rates.
if age < 5:
    price = 0
elif age <= 12:
    price = 50
elif age <= 59:
    price = 100
else:
    price = 70

print(price)
