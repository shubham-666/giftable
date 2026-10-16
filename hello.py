# print("hello, world.")
# name = "shubham"
name = "Shubham"
age = 25
A = '1'
B = '12'
C = '13'
D = '20'



greatest = int(A)

if int(B) > greatest:
    greatest = int(B)

if int(C) > greatest:
    greatest = int(C)

if int(D) > greatest:
    greatest = int(D)

print(greatest)



print(f"Hello, {name}! Next year you will be {age + 1}.")











age = int(input("Enter your age: "))

if age < 5:
    print("Ticket is free")
elif age <= 17:
    print("Half price")
elif age <= 59:
    print("Full price")
else:
    print("Concession price")