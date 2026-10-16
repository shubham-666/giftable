numbers = []
for i in range(1, 5):
    number = int(input(f"Enter number {i}: "))
    numbers.append(number)

greatest = numbers[0]
for number in numbers[1:]:
    if number > greatest:
        greatest = number

print("Greatest number:", greatest)
