class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.is_bankrupt = False
        self.is_loan_available = True
        self.total_loan_given = 0
        self.total_available_balance = 0

    def create_account(self, name, email, address, account_type):
        account_number = f'{name}{email}'
        self.accounts[account_number] = {
            "name": name,
            "email": email,
            "address": address,
            "account_type": account_type,
            "balance": 0,
            "loan_taken": 0,
            "transaction_history": []
        }
        print(f"Account created successfully and your account number is {account_number}!!")

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            print("Account deleted successfully")
        else:
            print("Account does not exist")

    def view_accounts(self):
        for account_number, details in self.accounts.items():
            print(f"Account Number: {account_number}, Name: {details['name']}, Email: {details['email']}, Address: {details['address']}, Account Type: {details['account_type']}")
            

        

class User:
    def __init__(self, bank, name, email, address):
        self.bank = bank
        self.name = name
        self.email = email
        self.address = address

    def create_account(self, name, email, address, account_type):
        self.bank.create_account(name, email, address, account_type)

    def deposit(self, account_number, amount):
        self.bank.accounts[account_number]['balance'] += amount
        self.bank.total_available_balance += amount
        print("Your money is diposited successfully !!")
        self.bank.accounts[account_number]["transaction_history"].append(f"Deposited: {amount}")

    def withdraw(self, account_number, amount):
        if self.bank.is_bankrupt == False:
            if self.bank.accounts[account_number]['balance'] >= amount :
                self.bank.accounts[account_number]['balance'] -= amount
                self.bank.total_available_balance -= amount
                print(f"Here is your money: {amount}")
                self.bank.accounts[account_number]['transaction_history'].append(f"Withdrawn: {amount}")
            else:
                print("Withdrawal amount exceeded")
        else:
            print("The bank is bankrupt !!")

    def check_available_balance(self, account_number):
        if self.bank.accounts[account_number]:
            print(f'Balance: {self.bank.accounts[account_number]['balance']}')
        else:
            print("Account does not exist")

    def check_transaction_history(self, account_number):
        if self.bank.accounts[account_number]:
            print("*****Transaction History*****")
            for transaction in self.bank.accounts[account_number]["transaction_history"]:
                print(transaction)
        else:
            print("Account does not exist")

    def take_loan(self, account_number, amount):
        if self.bank.accounts[account_number]:
            if self.bank.is_loan_available == True:
                if self.bank.accounts[account_number]['loan_taken'] < 2:
                    self.bank.accounts[account_number]['loan_taken'] += 1
                    self.bank.accounts[account_number]['balance'] -= amount
                    self.bank.total_available_balance -= amount
                    self.bank.total_loan_given += amount
                    print("Loan taken successfully")
                    self.bank.accounts[account_number]['transaction_history'].append(f"Loan taken: {amount}")
            else:
                print("Loan facility is not available :(")
        else:
            print("Account does not exist")

    def transfer_money(self, sender_account_number, receiver_account_number, amount):
        if self.bank.accounts[sender_account_number] and self.bank.accounts[receiver_account_number]:
            if self.bank.accounts[sender_account_number]['balance'] >= amount:
                self.bank.accounts[sender_account_number]['balance'] -= amount
                self.bank.total_available_balance -= amount
                self.bank.accounts[receiver_account_number]['balance'] += amount
                self.bank.total_available_balance += amount
                self.bank.accounts[sender_account_number]['transaction_history'].append(f"Transferred: {amount}")
                self.bank.accounts[receiver_account_number]['transaction_history'].append(f"Received: {amount}")
                print(f"Successfully Transferred to {receiver_account_number}")
            else:
                print("Insufficient balance")
        else:
            print("Account does not exist")

class Admin:
    def __init__(self, bank, name, email, address, account_type):
        self.bank = bank
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type

    def create_account(self, name, email, address, account_type):
        self.bank.create_account(name, email, address, account_type)

    def delete_account(self, account_number):
        if self.bank.accounts[account_number]:
            self.bank.delete_account(account_number)
        else:
            print("Account does not exist")
    
    def view_accounts(self):
        self.bank.view_accounts()

    def check_total_available_balance(self):
        print(f'Total available balance of the bank: {self.bank.total_available_balance}')

    def total_loan_given(self):
        print(f'Total loan given by the bank: {self.bank.total_loan_given}')

    def turn_on_or_off_loan(self):
        print('1. Turn on loan feature')
        print('2. Turn off loan feature')
        choice = int(input(f'Which option would you like to choose ?\t'))
        if choice == 1:
            self.bank.is_loan_available = True
            print('Loan feature turned on')
        elif choice == 2:
            self.bank.is_loan_available = False
            print('Loan feature turned off')
        else:
            print('Invalid choice')




    
class Main:
    bank = Bank('Baap er bank')
    while True:
        print(f'Welcome to {bank.name}!!')
        print("1. User")
        print("2. Admin")
        print("3. Exit")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            name = input("Enter Your Name : ")
            email = input("Enter Your Email : ")
            address = input("Enter Your Address : ")
            user = User(bank, name, email, address)

            while True:
                print(f"Welcome {name}")
                print("1. Create account")
                print("2. Deposit money")
                print("3. Withdraw money")
                print("4. Check balance")
                print("5. Check transaction history")
                print("6. Take loan")
                print("7. Transfer money")
                print("8. Exit")
                choice = int(input("Enter Your Choice : "))
                if choice == 1:
                    account_type = input('Enter your account type: ')
                    user.create_account(name, email, address, account_type)
                elif choice == 2:
                    account_number = input('Enter your account number: ')
                    amount = int(input('Enter the amount: '))
                    user.deposit(account_number, amount)
                elif choice == 3:
                    account_number = input('Enter your account number: ')
                    amount = int(input('Enter the amount: '))
                    user.withdraw(account_number, amount)
                elif choice == 4:
                    account_number = input('Enter your account number: ')
                    user.check_available_balance(account_number)
                elif choice == 5:
                    account_number = input('Enter your account number: ')
                    user.check_transaction_history(account_number)
                elif choice == 6:
                    account_number = input('Enter your account number: ')
                    amount = int(input('Enter the amount: '))
                    user.take_loan(account_number, amount)
                elif choice == 7:
                    sender_account_number = input('Enter your account number: ')
                    receiver_account_number = input('Enter receiver account number: ')
                    amount = int(input('Enter the amount: '))
                    user.transfer_money(sender_account_number, receiver_account_number, amount)
                elif choice == 8:
                    break
                else:
                    print("Invalid Input!!")
        elif choice == 2:
            name = input("Enter Your Name : ")
            email = input("Enter Your Email : ")
            address = input("Enter Your Address : ")
            admin = Admin(bank, name, email, address)
            while True:
                print(f"Welcome {name}")
                print("1. Create account")
                print("2. Delete account")
                print("3. View accounts")
                print("4. Check bank total available balance")
                print("5. Total loan given")
                print("6. Turn on or off loan")
                print("7. Exit")
                choice = int(input("Enter Your Choice : "))
                if choice == 1:
                    account_type = input('Enter your account type: ')
                    admin.create_account(name, email, address, account_type)
                elif choice == 2:
                    account_number = input('Enter your account number: ')
                    admin.delete_account(account_number)
                elif choice == 3:
                    admin.view_accounts()
                elif choice == 4:
                    admin.check_total_available_balance()
                elif choice == 5:
                    admin.total_loan_given()
                elif choice == 6:
                    admin.turn_on_or_off_loan()
                elif choice == 7:
                    break
                else:
                    print("Invalid Input!!")
        elif choice == 3:
            break
        else:
            print("Invalid Input!!")
    
Main()
# bank = Bank('bhitor_angngul')

# user1 = User(bank, 'zillur', 'zillur.hero40@gmail.com', '11/11/11', 'Savings')
# user2 = User(bank, 'rohan', 'zillur@gmail.com', '12/12/12', 'Current')
# user1.create_account('zillur', 'zillur.hero40@gmail.com', '11/11/11', 'Savings')
# user2.create_account('rohan', 'zillur@gmail.com', '12/12/12', 'Current')
    
# user1.deposit('zillurzillur.hero40@gmail.com', 10000)
# user1.withdraw('zillurzillur.hero40@gmail.com', 500)
# user1.take_loan('zillurzillur.hero40@gmail.com', 100)
# user1.transfer_money('zillurzillur.hero40@gmail.com', 'rohanzillur@gmail.com', 1000)
# user2.check_available_balance('rohanzillur@gmail.com',)
# user1.check_transaction_history('zillurzillur.hero40@gmail.com')

# print('********************************* ADMIN ********************************')

# admin1 = Admin(bank, 'adam', 'adam@gamil.com', 'h1, b2, atag, hong kong', 'Savings')
# admin1.create_account( 'adam', 'adam@gamil.com', 'h1, b2, atag, hong kong', 'Savings')
# admin1.view_accounts()
# admin1.check_total_available_balance()
# admin1.total_loan_given()
# admin1.turn_on_or_off_loan()