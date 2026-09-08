a, b = map(int, input("Enter two numbers: ").split())
a ^= b
b ^= a
a ^= b
print(a, b)
