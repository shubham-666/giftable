# Plan:
# 1. Read a whole number from the user.
# 2. Numbers below 2 are not prime.
# 3. Start checking possible divisors from 2.
# 4. If the number is divisible by a divisor, print the divisor.
# 5. Mark the number as not prime and stop checking.
# 6. Otherwise, move to the next divisor.
# 7. Stop once the divisor is large enough that no further check is needed.
# 8. Print whether the number is prime.


number = int(input("Enter a number: "))

if number < 2:
    print(number, "is not prime")
else:
    divisor = 2
    is_prime = True

    while divisor * divisor <= number:
        if number % divisor == 0:
            print(number, "is divisible by", divisor)
            is_prime = False
            break

        divisor += 1

    if is_prime:
        print(number, "is prime")
    else:
        print(number, "is not prime")