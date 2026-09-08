a, b, c = map(float, input("Enter three sides: ").split())
print("Valid triangle" if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a else "Invalid triangle")
