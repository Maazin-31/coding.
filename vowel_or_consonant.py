ch = input("Enter a character: ").strip()
if len(ch) != 1 or not ch.isalpha():
    print("Invalid input")
else:
    print("Vowel" if ch.lower() in "aeiou" else "Consonant")
