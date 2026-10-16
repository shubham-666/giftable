number = int(input("Enter an integer: "))
if number < 2:
    print(number, "is not prime.")
else:
    is_prime = True
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

    if is_prime:
        print(number, "is prime.")
    else:
        print(number, "is not prime.")
