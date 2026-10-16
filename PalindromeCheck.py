# Plan:
# 1. Read a whole number from the user.
# 2. Keep the original number because we need it for comparison.
# 3. Make a copy of the number for reversing.
# 4. Extract the last digit using %.
# 5. Build the reversed number.
# 6. Remove the last digit using //.
# 7. Repeat until the number becomes zero.
# 8. Compare the reversed number with the original number.
# 9. If they are equal, the number is a palindrome.
# 10. Otherwise, it is not a palindrome.


number = int(input("Enter a number: "))

original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print(original, "reversed is", reverse)

if original == reverse:
    print("Result: Palindrome")
else:
    print("Result: Not Palindrome")