n = int(input("Enter n: "))
k = int(input("Enter k (0-based): "))
print("Set" if (n & (1 << k)) else "Not set")
