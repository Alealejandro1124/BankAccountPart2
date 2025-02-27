#test_bank_account.py
#Used ChatGPT to learn how to build test files in Python

# Import the BankAccount class from bank_account.py
from bank_account import BankAccount

def main():
    """
    Main function to test the BankAccount class.
    Tests two instances.
    """

    #Create the first account
    account1 = BankAccount("Victoria", 10022.00,500.00, 123243225, 103214567)

    #test deposits
    account1.deposit(1500.00)

    #Test withdraw above minimum balance
    account1.withdraw(500.00)

    #Test withdraw below minimum balance
    account1.withdraw(11000.00)

    #Print customer info
    account1.print_customer_information()

    #Create a second account
    account2 = BankAccount("Kevin", 53000,2500, 3426536345, 103214567)

    #Make a deposit
    account2.deposit(15000)

    #Make a withdraw above minimum
    account2.withdraw(25000)

    #Make a withdraw below minimum
    account2.withdraw(50000)

    #Print customer information
    account2.print_customer_information()

if __name__ == "__main__":
    main()

