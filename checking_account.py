# checking_account.py

from bank_account import BankAccount

class CheckingAccount(BankAccount):
    """ Checking account subclass with a transfer limit."""

    def __init__(self, customer_name, current_balance, minimum_balance,
                 account_number, routing_number, transfer_limit):
        """
        Constructor for CheckingAccount.
        Inherits from BankAccount and adds transfer limit.

        :param transfer_limit: float - Maximum amount allowed per transfer.
        """

        super(CheckingAccount, self).__init__(customer_name, current_balance,
                                              minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit #Additional attribute for transfer limit.

    def transfer(self, amount, destination_account):
        """
        Transfers money from checking to another account.

        :param amount: float - Amount to transfer.
        :param destination_account: SavingsAccount - Account to transfer to.
        """
        if amount > self.transfer_limit:
            print(f"Transfer limit exceeded! Max allowed per transfer: ${self.transfer_limit:.2f}\n")
        elif self.current_balance - amount >= self.minimum_balance:
            self.current_balance -= amount
            destination_account.current_balance += amount #Add amount to savings account

            #Extract last 4 digits of accounts
            checking_last4 = str(self._account_number)[-4:]
            savings_last4 = str(destination_account._account_number)[-4:]

            print(f"Transfer of ${amount:.2f} from Checking Account: *****{checking_last4}"
                  f" to Savings Account: *****{savings_last4} successful.")
            print(f"New Checking Balance for Account *****{checking_last4}: ${self.current_balance:.2f}")
            print(f"New Savings Balance for Account *****{savings_last4}: ${destination_account.current_balance:.2f}\n")
        else:
            print("Error: Insufficient funds for transfer.\n")