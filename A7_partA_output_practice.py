# Assignment practice: predict the output before running this file.
# Write your predictions on paper, then run the program and compare.

print("BLOCK 1")
x = 5
print(x + 2)

print("BLOCK 2")
for i in range(1, 4):
    print(i, end=" ")
print()

print("BLOCK 3")
values = [2, 4, 6]
values.append(8)
print(values)

print("BLOCK 4")
try:
    print(10 // 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
