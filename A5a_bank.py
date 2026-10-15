class Bank:
    def __init__(self, opening_balance=0.0):
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative.")
        self.__balance = float(opening_balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return
        self.__balance += amount
        print(f"Deposited ₹{amount:.2f}.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > self.__balance:
            print("Withdrawal refused: insufficient balance.")
        else:
            self.__balance -= amount
            print(f"Withdrew ₹{amount:.2f}.")

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    opening = float(input("Enter opening balance: ₹"))
    account = Bank(opening)

    while True:
        print("\\n1. Deposit  2. Withdraw  3. Show balance  4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            account.deposit(float(input("Amount to deposit: ₹")))
        elif choice == "2":
            account.withdraw(float(input("Amount to withdraw: ₹")))
        elif choice == "3":
            print(f"Current balance: ₹{account.get_balance():.2f}")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
