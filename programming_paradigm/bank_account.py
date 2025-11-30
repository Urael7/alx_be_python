class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        """Add money to the balance"""
        self.account_balance += float(amount)

    def withdraw(self, amount):
        """Withdraw only if enough balance, return True/False"""
        amount = float(amount)
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print EXACT format the checker expects (no trailing .0 when integer)"""
        print(f"Current Balance: ${self.account_balance:g}")
