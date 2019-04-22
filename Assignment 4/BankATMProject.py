import sys
def verify_pin(pin):
    if pin == "1234":
        return True
    else:
        return False

def log_in():
    tries = 0
    while tries < 4:
        pin = input('Please Enter Your 4 Digit Pin: ')
        if verify_pin(pin):
            print("Pin accepted!")
            return True
        else:
            print("Invalid pin. Sorry Try Again !!!")
            tries += 1
    print("Too many incorrect tries. Could not log in")
    return False

def start_menu():
    print("Welcome to the ATM!")
    if log_in():
        main_menu()
    print("Thank you for using Bank of Wealth ATM")


def main_menu():
    print("""
    Welcome to the Bank of Wealth !!!

    To continue please follow the instructions:
    Select options:
        (1) New Account 
        (2) Withdraw
        (3) Deposit
        (4) Balance Inquiry
        (5) Demand Draft
        (6) Cancel
    """)
    choice = int(input("> "))
    if choice == 1:
        new_account()
    elif choice == 2:
        withdraw()
    elif choice == 3:
        deposit()
    elif choice == 4:
        balance_inquiry()
    elif choice == 5:
        demand_draft()
    else:
        print("Exiting...")

def new_account():
    name = input("Please Enter First Name and Last Name: ")
    age = int(input("Please Enter age: "))
    address = input("Please Enter Address: ")
    contact = int(input("Please Enter your Phone number: "))
    gender = input("Please Enter Male or Female as gender: ")
    print(f"{name},{age}, {address}, {contact}, {gender}")
    back()

def withdraw():
    withdraw = float(input('How Much Would you like to withdraw ?: '))
    if withdraw in range(100,10001):
        print("Here is your Money", withdraw)
    else:
        print("LIMIT EXCEEDED")
    back()

def deposit():
    amount = int(input("Please enter the depsit amount: "))
    if amount%5==0:
        print(amount)
    else:
        print("Enter the Valid Amount")
    back()

def balance_inquiry():
    print("""
    Please make a Selection:
    (1) Deposit amount
    (2) Outstanding Balance
    (3) Minimum Due Amount
    """)
    prefer = int(input("Please make a Selection from the options: "))
    if prefer == 1:
        print("Deposit Amount")
    elif prefer == 2:
        print("Outstanding Balance")
    else:
        print("Minimum Due Balance")
    back()

def demand_draft():
    bank = input("Please Enter the name of bank: ")
    holder = input("Please Enter the name of Account Holder: ")
    branch = input("Please Enter the name of Branch: ")
    amount = int(input("Please Enter the amount for Demand Draft: "))
    print(f"{bank}, {holder}, {branch}, {amount}")
    back()

def back():
    user = input("Would you like to continue with options or Quit ? (Yes/No): ").lower()
    if user == 'yes':
        main_menu()
    else:
        print("Thank you for using Bank of Wealth ATM")
        sys.exit(1)



start_menu()