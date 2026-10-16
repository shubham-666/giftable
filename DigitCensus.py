# Plan:
# 1. Read a whole number from the user.
# 2. Create counters for even, odd, and zero digits.
# 3. Take the last digit using %.
# 4. Check zero first because zero is even but belongs in its own group.
# 5. If the digit is not zero, check whether it is even or odd.
# 6. Remove the last digit using 
# 7. Repeat until all digits have been checked.
# 8. Print the three counts.


number = int(input("Enter a number: "))

even_count = 0
odd_count = 0
zero_count = 0

while number > 0:
    digit = number % 10

    if digit == 0:
        zero_count += 1
    elif digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    number = number // 10

print("Even digits :", even_count)
print("Odd digits  :", odd_count)
print("Zero digits :", zero_count)