x, y = map(float, input("Enter x and y coordinates: ").split())

if x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("Y-axis")
elif y == 0:
    print("X-axis")
elif x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
else:
    print("Quadrant IV")
