import cmath

a, b, c = map(float, input("Enter a, b, c: ").split())

if a == 0:
    print("Not a quadratic equation")
else:
    d = b * b - 4 * a * c

    if d > 0:
        r1 = (-b + d ** 0.5) / (2 * a)
        r2 = (-b - d ** 0.5) / (2 * a)
        print("Real and distinct roots:", r1, r2)
    elif d == 0:
        r = -b / (2 * a)
        print("Real and equal roots:", r)
    else:
        r1 = (-b + cmath.sqrt(d)) / (2 * a)
        r2 = (-b - cmath.sqrt(d)) / (2 * a)
        print("Imaginary roots:", r1, r2)
