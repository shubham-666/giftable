# Plan:
# 1. Use an outer loop for the numbers 1 to 5.
# 2. For each row, start with an empty piece of text.
# 3. Use an inner loop for the numbers 1 to 5.
# 4. Multiply the row number by the column number.
# 5. Format each result to five characters wide and right-aligned.
# 6. Add each formatted result to the row.
# 7. Print the complete row after the inner loop finishes.


for row in range(1, 6):
    line = ""

    for column in range(1, 6):
        result = row * column
        line += f"{result:5}"

    print(line)