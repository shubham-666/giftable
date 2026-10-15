cities = []
while True:
    city = input("Enter a city (or type 'done' to finish): ").strip()
    if city.lower() == "done":
        break
    if city:
        cities.append(city)

print("Cities:", cities)

remove_city = input("Enter a city to remove (or press Enter to skip): ").strip()
if remove_city:
    if remove_city in cities:
        cities.remove(remove_city)
        print("Removed:", remove_city)
    else:
        print("That city is not in the list.")

print("Final city list:")
for city in cities:
    print(city)
