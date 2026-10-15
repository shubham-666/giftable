number = int(input("Enter a positive integer: "))
if number < 1:
    print("Please enter a positive integer.")
else:
    print("Collatz sequence:", end=" ")
    while number != 1:
        print(number, end=" -> ")
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1
    print(1)
