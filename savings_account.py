# savings_account.py

from bank_account import BankAccount # Importing base class

class SavingsAccount(BankAccount):
    """Savings account subclass with interest rate functionality."""

    def __init__(self, customer_name, current_balance, minimum_balance,
                 account_number, routing_number, interest_rate):
        """
        Constructor for SavingsAccount.
        Inherits from BankAccount, adds interest rate functionality.

        :param interest_rate: float - percentage of interest
        """

        super().__init__(customer_name,current_balance,minimum_balance,
                            account_number, routing_number)
        self.interest_rate = interest_rate #Additional attribute for interest

    def apply_interest(self ):
        """ Applies interest to the current balance. """
        interest = self.interest_rate * self.current_balance
        self.current_balance += interest
        print(f"Interest of ${interest:.2f} applied, New balance is ${self.current_balance:.2f}\n")

