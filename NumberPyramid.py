# Plan:
# 1. Read the number of rows from the user.
# 2. Use a loop for each row from 1 to the requested number of rows.
# 3. Calculate the spaces needed before the numbers.
# 4. The number of spaces decreases as the row number increases.
# 5. Build the numbers from 1 up to the current row.
# 6. Print the spaces followed by the numbers for that row.


rows = int(input("Enter rows: "))

for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    numbers = ""

    for j in range(1, i + 1):
        numbers += str(j) + " "

    print(spaces + numbers)