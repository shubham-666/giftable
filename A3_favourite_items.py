items = []
count = int(input("How many favourite items do you want to enter? "))

for i in range(count):
    item = input(f"Enter favourite item {i + 1}: ").strip()
    items.append(item)

print("Your favourite items:")
for item in items:
    print("-", item)
