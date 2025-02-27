#bank_account.py

class BankAccount:
    """
    BankAccount class to model transactions
    and enforce a minimum balance.
    """

    #Class Attribute
    bank_name = "Bank of Alejandro"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
       """
       Constructor for BankAccount class.

       :param customer_name: str - Name of customer
       :param current_balance: float - Starting balance
       :param minimum_balance: float - Minimum balance
                                    (withdrawals cannot go below)
       :param account_number: str - Account number
                                    (Protected attribute, visible to subclasses)
       :param routing_number: str - Routing number
                                    (Private attribute, not directly accessible)
       """
       # Instance Attributes
       self.customer_name = customer_name
       self.current_balance = current_balance
       self.minimum_balance = minimum_balance
       self._account_number = account_number #Protected Member
       self.__routing_number = routing_number #Private Member

    def deposit(self, amount):
        """
        Increase the current balance by the amount specified.
        :param amount:
        """
        self.current_balance += amount
        print(f"Deposit of ${amount:.2f} accepted. New balance: ${self.current_balance:.2f}\n")

    def withdraw(self, amount):
        """
        Decrease the current balance by the amount specified.
        :param amount:
        """
        if self.current_balance - amount >= self.minimum_balance:
            self.current_balance -= amount
            print(f"Withdrawal of ${amount:.2f} accepted. New balance: ${self.current_balance:.2f}\n")
        else:
            print(f"Withdrawal denied. New balance would be below minimum balance of ${self.minimum_balance:.2f}.\n")

    def get_account_number(self):
        """Getter for the protected account number."""
        return self._account_number

    def get_routing_number(self):
        """Getter for the private routing number."""
        return self.__routing_number

    def print_customer_information(self):
        """
        Print bank name, customer name,routing number, account number, and current balance.
        """
        masked_account_number = "*****" + str(self._account_number)[-4:] #Provide only last 4 digits
        print(f"Bank name: {self.bank_name}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Routing Number: {self.get_routing_number()}") #Routing Number
        print(f"Account Number: {masked_account_number}") #masked account number
        print(f"Current Balance: ${self.current_balance:.2f}")
        print(f"Minimum Balance: ${self.minimum_balance:.2f}")
        print("-------------------------\n")
