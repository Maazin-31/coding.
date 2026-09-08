marks = float(input("Enter marks (0-100): "))

if not 0 <= marks <= 100:
    print("Invalid marks")
elif marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")
