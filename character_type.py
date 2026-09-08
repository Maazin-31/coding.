ch = input("Enter a character: ").strip()

if len(ch) != 1:
    print("Invalid input")
elif ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")
