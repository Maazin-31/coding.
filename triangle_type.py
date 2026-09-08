a, b, c = map(float, input("Enter three sides: ").split())

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Invalid triangle")
elif a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")
