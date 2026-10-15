number = input("Enter a whole number: ").strip()
if number.startswith("-"):
    digits = number[1:]
else:
    digits = number

if not digits.isdigit():
    print("Please enter a valid whole number.")
else:
    print("Number of digits:", len(digits))
    print("Zeroes:", digits.count("0"))
    print("Even digits:", sum(1 for ch in digits if int(ch) % 2 == 0))
    print("Odd digits:", sum(1 for ch in digits if int(ch) % 2 != 0))
