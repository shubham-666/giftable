cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore"]

print("First city:", cities[0])
print("Last city:", cities[-1])
print("Number of cities:", len(cities))

cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore"]

cities[2] = "Pune"
cities.append("Hyderabad")

print("Updated list:", cities)


food1 = input("Enter your first favourite food: ")
food2 = input("Enter your second favourite food: ")
food3 = input("Enter your third favourite food: ")

foods = [food1, food2, food3]

print(f"You like {foods[0]}, {foods[1]} or {foods[2]}.")