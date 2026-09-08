n = int(input("Enter a non-negative integer: "))
count = 0
while n:
    n &= n - 1
    count += 1
print(count)
