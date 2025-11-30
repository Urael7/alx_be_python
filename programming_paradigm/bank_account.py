class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        """Deposit money into the account."""
        self.account_balance += float(amount)

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist. Return True if successful, else False."""
        amount = float(amount)
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance in EXACT format for ALX checker."""
        print(f"Current Balance: ${self.account_balance:g}")
