# main.py file to test functionality of checking_account.py and savings_account.py

from checking_account import CheckingAccount
from savings_account import SavingsAccount

def scenario_separator():
    """"Print seperator to distinguish scenarios"""
    print("-"*80 + "\n")

#Scenario 1: A user opens a Checking and Savings Account.

print("""Scenario 1: Creating new accounts and printing initial details\n""")

checking = CheckingAccount("Nathan", 5000, 100,
                           9893436767, 103214567, 2500)
savings = SavingsAccount("Nathan", 3000, 100,
                         103432342, 103214567, .02)

checking.print_customer_information()   #Print Checking Account Details
savings.print_customer_information()    #Print Savings Account Details

scenario_separator()

#Scenario 2: Depositing money into both accounts

print("Scenario 2: Depositing funds into newly created accounts\n")

checking.deposit(750)  # Deposit into Checking
savings.deposit(1750)  # Deposit into Savings

scenario_separator()

#Scenario 3: Withdrawing funds from both accounts

print("Scenario 3: Withdrawing funds from newly created accounts\n")
checking.withdraw(750)  # Withdraw from Checking
savings.withdraw(1750)  # Withdraw from Savings

scenario_separator()

#Scenario 4: Attempting to withdraw below minimum allowed balance

print("Scenario 4: Attempting to withdraw funds below minimum allowed balance\n")
checking.withdraw(5000) #Attempt to withdraw amount that violates minimum balance required
savings.withdraw(3000)  #Attempt to withdraw amount that violates minimum balance required

scenario_separator()

#Scenario 5: Applying interest to Savings Account

print("Scenario 5: Applying interest to Savings Account\n")

savings.apply_interest() # Apply interest to Savings Account

scenario_separator()

#Scenario 6: Attempting to transfer that exceeds transfer limit

print("Scenario 6: Transfer exceeding transfer limit\n")

checking.transfer(2750, savings) #Attempt to transfer more than allowed limit

scenario_separator()

#Scenario 7: Successful transfer from Checking to Savings

print("Scenario 7: Successful transfer from Checking to Savings\n")

checking.transfer(2000, savings) # Transfer within the limit

scenario_separator()

#Scenario 8: Creating a second set of Checking and Savings Accounts
print("Creating second account instances\n")

checking2 = CheckingAccount("Anna", 7000, 1000,
                            948833076, 103214567, 5000)
savings2 = SavingsAccount("Anna", 10000, 5000,
                          948736348, 103214567, .045)

checking2.print_customer_information()  # Print Second Checking Account Details
savings2.print_customer_information()   # Print Second Savings Account Details

scenario_separator()

#Scenario 9: Performing Transactions on second set of accounts

print("Scenario 9: Multiple transcations on second set of accounts\n")

checking2.withdraw(6500) # Withdraw over minimum balance limit
checking2.withdraw(2500) # Withdraw within limit
checking2.transfer(5500, savings2) # Transfer over transfer limit
checking2.transfer(5000, savings2) # Transfer within limit but under current balance
checking2.transfer(2500, savings2) # Successful Transfer
savings2.withdraw(5500) # Withdraw within minimum balance limit
savings2.withdraw(2500) # Withdraw over minimum balance limits
savings2.deposit(7500) # Deposit into Savings
savings2.apply_interest() #Apply interest to current savings account balance
