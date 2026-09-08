units = float(input("Enter units consumed: "))

# Example slab rates because the supplied question does not specify exact rates.
# 0-100: ₹1.50/unit, 101-200: ₹2.50/unit, 201-500: ₹4.00/unit, above 500: ₹6.00/unit
if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 1.50
elif units <= 200:
    bill = 100 * 1.50 + (units - 100) * 2.50
elif units <= 500:
    bill = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00
else:
    bill = 100 * 1.50 + 100 * 2.50 + 300 * 4.00 + (units - 500) * 6.00

if units >= 0:
    print(f"{bill:.2f}")
