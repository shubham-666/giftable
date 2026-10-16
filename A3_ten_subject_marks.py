marks = []
for i in range(1, 11):
    mark = float(input(f"Enter marks for subject {i} (0-100): "))
    while not 0 <= mark <= 100:
        print("Marks must be between 0 and 100.")
        mark = float(input(f"Enter marks for subject {i} (0-100): "))
    marks.append(mark)

print("Marks:", marks)
print("Highest marks:", max(marks))
print("Lowest marks:", min(marks))
print(f"Average marks: {sum(marks) / len(marks):.2f}")
