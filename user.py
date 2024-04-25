class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}
        self.is_bankrupt = False

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
        print(f"Account created successfully  and your account number is {account_number}!!")

class User:
    def __init__(self, bank, name, email, address, account_type):
        self.bank = bank
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type

    def create_account(self, name, email, address, account_type):
        self.bank.create_account(name, email, address, account_type)

    def deposit(self, account_number, amount):
        self.bank.accounts[account_number]['balance'] += amount
        self.bank.accounts[self.account_number]["transaction_history"].append(f"Deposited: {amount}")

    def withdraw(self, account_number, amount):
        if self.is_bakrupt == False:
            if self.balance >= amount :
                self.bank.accounts[account_number]['balance'] -= amount
                self.bank.accounts[self.account_number]['transaction_history'].append(f"Withdrawn: {amount}")
            else:
                print("Withdrawal amount exceeded")
        else:
            print("The bank is bankrupt !!")

    def check_available_balance(self, account_number):
        print(self.bank.accounts[account_number]['balance'])

    def check_transaction_history(self):
        print("*****Transaction History*****")
        for transaction in self.bank.accounts[self.account_number]["transaction_history"]:
            print(transaction)

    def take_loan(self, account_number, amount):
        if self.bank.accounts[account_number]['loan_taken'] < 2:
            self.bank.accounts[account_number]['loan_taken'] += 1
            self.bank.accounts[account_number]['balance'] -= amount
            self.bank.accounts[account_number]['transaction_history'].append(f"Loan taken: {amount}")

    def transfer_money(self, sender_account_number, receiver_account_number, amount):
        if self.bank.accounts[sender_account_number] and self.bank.accounts[receiver_account_number]:
            if self.bank.accounts[sender_account_number]['balance'] >= amount:
                self.bank.accounts[sender_account_number]['balance'] -= amount
                self.bank.accounts[receiver_account_number]['balance'] += amount
                self.bank.accounts[sender_account_number]['transaction_history'].append(f"Transferred: {amount}")
                self.bank.accounts[receiver_account_number]['transaction_history'].append(f"Received: {amount}")
            else:
                print("Insufficient balance")
        else:
            print("Account does not exist")

bank = Bank('bhitor_angngul')

user1 = User(bank, 'zillur', 'zillur.hero40@gmail.com', '11/11/11', 'Savings')
user1.create_account('zillur', 'zillur.hero40@gmail.com', '11/11/11', 'Savings')
    
