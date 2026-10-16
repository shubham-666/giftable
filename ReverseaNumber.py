# Plan:
# 1. Read a whole number from the user.
# 2. Keep a copy of the original number.
# 3. Take the last digit using the % operator.
# 4. Add that digit to the reversed number.
# 5. Remove the last digit from the number using //.
# 6. Repeat until there are no digits left.
# 7. Print the reversed number.


number = int(input("Enter a number: "))

original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reverse of", original, "is", reverse)