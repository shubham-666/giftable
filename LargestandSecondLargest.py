# Decision:
# If the largest number appears twice, the second largest means
# the second distinct-largest value.
#
# Plan:
# 1. Read five numbers one at a time.
# 2. Do not store the numbers in a list.
# 3. Keep track of the largest number seen so far.
# 4. Keep track of the second largest distinct number.
# 5. If a new number is larger than the largest, move the old largest
#    into the second-largest position.
# 6. Otherwise, if the number is smaller than the largest but larger
#    than the current second largest, update the second largest.
# 7. Repeat for all five numbers.
# 8. Print the largest and second largest numbers.


largest = None
second_largest = None

for i in range(5):
    number = int(input("Enter number: "))

    if largest is None or number > largest:
        second_largest = largest
        largest = number

    elif number < largest and (second_largest is None or number > second_largest):
        second_largest = number

print("Largest       :", largest)
print("Second largest:", second_largest)