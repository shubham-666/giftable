class Player:
    def __init__(self, name):
        self.name = name
        self.bag = []

    def add_item(self, item):
        if item in self.bag:
            print("You already have", item)
        else:
            self.bag.append(item)
            print(item, "added to your bag.")

    def show_bag(self):
        print("\nYour bag:")

        if len(self.bag) == 0:
            print("Bag is empty.")
        else:
            for item in self.bag:
                print("-", item)

    def has_item(self, item):
        return item in self.bag


class Place:
    def __init__(self, name, description, item=None):
        self.name = name
        self.description = description
        self.item = item

    def visit(self):
        print("\nYou are at", self.name)
        print(self.description)

    def take_item(self, player):
        if self.item is None:
            print("There is nothing here to take.")
        elif player.has_item(self.item):
            print("You already took", self.item)
        else:
            player.add_item(self.item)
            self.item = None


class LockedPlace(Place):
    def __init__(self, name, description, required_item, item=None):
        super().__init__(name, description, item)
        self.required_item = required_item
        self.is_open = False

    def visit(self):
        print("\nYou are outside the", self.name)
        print("The door is locked.")

    def enter(self, player):
        if player.has_item(self.required_item):
            self.is_open = True
            print("You used the", self.required_item)
            print("You entered the", self.name)
        else:
            print("You cannot enter.")
            print("You need the", self.required_item)

    def take_item(self, player):
        if not self.is_open:
            print("Enter the lab first.")
        else:
            super().take_item(player)


class Chest:
    def __init__(self, required_item):
        self.required_item = required_item
        self.is_open = False

    def open_chest(self, player):
        if self.is_open:
            print("The chest is already open.")
        elif player.has_item(self.required_item):
            self.is_open = True
            print("\nYou entered the secret code.")
            print("The chest is open!")
            print("You found the trophy!")
            print("Congratulations!")
        else:
            print("The chest is locked.")
            print("You need the", self.required_item)


# Creating player
player = Player("Student")

# Creating places
canteen = Place(
    "Canteen",
    "There is a small key on a table.",
    "key"
)

lab = LockedPlace(
    "Computer Lab",
    "There is something important inside the lab.",
    "key",
    "secret code"
)

stage = Place(
    "Main Stage",
    "There is a trophy chest on the stage."
)

chest = Chest("secret code")


while True:

    print("\n------ Missing Fest Trophy ------")
    print("1. Visit Canteen")
    print("2. Take Key")
    print("3. Visit Computer Lab")
    print("4. Enter Computer Lab")
    print("5. Take Secret Code")
    print("6. Visit Main Stage")
    print("7. Open Chest")
    print("8. Check Bag")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        canteen.visit()

    elif choice == "2":
        canteen.take_item(player)

    elif choice == "3":
        lab.visit()

    elif choice == "4":
        lab.enter(player)

    elif choice == "5":
        lab.take_item(player)

    elif choice == "6":
        stage.visit()

    elif choice == "7":
        chest.open_chest(player)

    elif choice == "8":
        player.show_bag()

    elif choice == "9":
        print("Game ended.")
        break

    else:
        print("Please enter a valid choice.")