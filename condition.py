import datetime

class BankingSystem:
    def __init__(self, account_holder, account_number, pin):
        self.account_holder = account_holder
        self.account_number = account_number
        self.pin = pin
        self.balance = 0
        self.transaction_history = []
        self.is_verified = False
        self.first_deposit_done = False

    def verify_account(self, pin_input):
        if self.pin == pin_input:
            self.is_verified = True
            print(" PIN verified successfully.")
        else:
            print(" Incorrect PIN. Please try again.")

    def deposit(self, amount):
        if not self.is_verified:
            print(" Please verify your account first.")
            return
        if amount <= 0:
            print(" Deposit amount must be positive.")
            return
        if not self.first_deposit_done:
            bonus = amount * 0.05
            amount += bonus
            self.first_deposit_done = True
            print(f" First deposit bonus added: {bonus:.2f}")

        self.balance += amount
        transaction = {
            "type": "Deposit",
            "amount": amount,
            "date": datetime.datetime.now()
        }
        self.transaction_history.append(transaction)
        print(f" Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if not self.is_verified:
            print(" Please verify your account first.")
            return
        if amount <= 0:
            print(" Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print(" Insufficient balance.")
            return

        self.balance -= amount
        transaction = {
            "type": "Withdrawal",
            "amount": amount,
            "date": datetime.datetime.now()
        }
        self.transaction_history.append(transaction)
        print(f" Withdrawn {amount}. New balance: {self.balance}")

    def get_balance(self):
        if not self.is_verified:
            print(" Please verify your account first.")
            return
        print(f" Current balance: {self.balance}")

    def get_transaction_history(self):
        if not self.is_verified:
            print(" Please verify your account first.")
            return
        if not self.transaction_history:
            print("ℹ No transactions found.")
            return
        print(f"\n Transaction history for {self.account_holder}:")
        for t in self.transaction_history:
            print(f"{t['date']} - {t['type']}: {t['amount']}")

def main():
    print(" Welcome to Bank Asia!")

    name = input(" Enter Your Name: ")
    acc_no = input(" Enter Your Account Number: ")
    pin = input(" Set a 4-digit PIN: ")

    account = BankingSystem(name, acc_no, pin)

    pin_input = input(" Enter your PIN to verify account: ")
    account.verify_account(pin_input)

    if account.is_verified:
        while True:
            print("\n Choose an option:")
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Exit")

            choice = input(" Enter Your Choice (1-5): ")
            if choice == "1":
                amount = float(input(" Enter amount to deposit: "))
                account.deposit(amount)

            elif choice == "2":
                amount = float(input(" Enter amount to withdraw: "))
                account.withdraw(amount)

            elif choice == "3":
                account.get_balance()

            elif choice == "4":
                account.get_transaction_history()

            elif choice == "5":
                print(" Thank you for using Bank Asia. Goodbye!")
                break

            else:
                print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
