a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

a, b = abs(a), abs(b)
while b != 0:
    a, b = b, a % b

print("Greatest common divisor:", a)
