a, b, c = map(int, input("Enter three numbers: ").split())

if a <= b:
    if b <= c:
        x, y, z = a, b, c
    elif a <= c:
        x, y, z = a, c, b
    else:
        x, y, z = c, a, b
else:
    if a <= c:
        x, y, z = b, a, c
    elif b <= c:
        x, y, z = b, c, a
    else:
        x, y, z = c, b, a

print(x, y, z)
