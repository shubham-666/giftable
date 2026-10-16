size = int(input("Enter the multiplication-grid size: "))
if size < 1:
    print("Size must be at least 1.")
else:
    for row in range(1, size + 1):
        for col in range(1, size + 1):
            print(f"{row * col:4}", end="")
        print()
