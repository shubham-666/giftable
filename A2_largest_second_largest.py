values = input("Enter integers separated by spaces: ").split()
numbers = [int(value) for value in values]

if len(numbers) < 2:
    print("Please enter at least two numbers.")
else:
    largest = max(numbers)
    distinct_smaller = [number for number in numbers if number < largest]
    if not distinct_smaller:
        print("Largest number:", largest)
        print("There is no distinct second-largest number.")
    else:
        print("Largest number:", largest)
        print("Second-largest distinct number:", max(distinct_smaller))
