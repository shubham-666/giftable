class Player:
    def __init__(self, name):
        self.name = name
        self.bag = []

    def collect(self, item):
        self.bag.append(item)
        print(f"{self.name} collected: {item}")

    def has_item(self, item):
        return item in self.bag


class Place:
    def __init__(self, name, item=None, required_item=None):
        self.name = name
        self.item = item
        self.required_item = required_item

    def visit(self, player):
        print(f"\\nVisiting {self.name}...")
        if self.required_item and not player.has_item(self.required_item):
            print(f"Access denied! You need {self.required_item}.")
            return False
        print(f"Entered {self.name}.")
        if self.item:
            player.collect(self.item)
            self.item = None
        return True


class CodeChest:
    def __init__(self, correct_code):
        self.correct_code = correct_code
        self.opened = False

    def open(self, code):
        if code == self.correct_code:
            self.opened = True
            print("Correct code! The trophy chest opens. You win!")
            return True
        print("Wrong code. The chest stays locked.")
        return False


def run_failed_route():
    print("\\n========== FAILED ROUTE ==========")
    player = Player("Player")
    canteen = Place("Canteen", item="key")
    lab = Place("Computer Lab", item="secret code", required_item="key")
    stage = Place("Main Stage", required_item="secret code")
    chest = CodeChest("FEST2026")

    # The player tries to go straight to the stage without collecting anything.
    stage.visit(player)
    print("The trophy remains locked. Route failed.")


def run_winning_route():
    print("\\n========== WINNING ROUTE ==========")
    player = Player("Player")
    canteen = Place("Canteen", item="key")
    lab = Place("Computer Lab", item="secret code", required_item="key")
    stage = Place("Main Stage", required_item="secret code")
    chest = CodeChest("FEST2026")

    canteen.visit(player)
    if lab.visit(player):
        # In the story, the lab reveals the code.
        print("The secret code is FEST2026.")
        player.collect("FEST2026")
    if stage.visit(player):
        chest.open(input("Enter the trophy chest code: ").strip().upper())


if __name__ == "__main__":
    run_failed_route()
    run_winning_route()
