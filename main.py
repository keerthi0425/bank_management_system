class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def display(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")


def main():
    accounts = {}

    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Account")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            accounts[name] = BankAccount(name)
            print("Account created!")

        elif choice == "2":
            name = input("Enter name: ")
            amount = float(input("Enter amount: "))
            if name in accounts:
                accounts[name].deposit(amount)
            else:
                print("Account not found!")

        elif choice == "3":
            name = input("Enter name: ")
            amount = float(input("Enter amount: "))
            if name in accounts:
                accounts[name].withdraw(amount)
            else:
                print("Account not found!")

        elif choice == "4":
            name = input("Enter name: ")
            if name in accounts:
                accounts[name].display()
            else:
                print("Account not found!")

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
