# Example ticket-price slabs; replace rates if your teacher gave different rules.
age = int(input("Enter your age: "))
if age < 0:
    print("Age cannot be negative.")
elif age < 5:
    price = 0
    print("Ticket price: ₹", price, "(free for children under 5)")
elif age <= 12:
    price = 100
    print("Ticket price: ₹", price)
elif age < 60:
    price = 200
    print("Ticket price: ₹", price)
else:
    price = 120
    print("Ticket price: ₹", price, "(senior discount)")
