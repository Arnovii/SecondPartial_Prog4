class Branch:
    def __init__(self, node_code, name, address, phone):
        self.node_code = node_code
        self.name = name
        self.address = address
        self.phone = phone

    def create(self):
        print(f"Branch '{self.name}' created")

    def delete(self):
        print(f"Branch '{self.name}' deleted")


class Employee(Branch):
    def __init__(self, node_code, name, address, phone, employee_id, position):
        super().__init__(node_code, name, address, phone)
        self.employee_id = employee_id
        self.position = position

    def show_info(self):
        print(f"Employee: {self.name}, Position: {self.position}")

    def change_position(self, new_position):
        self.position = new_position


class Client(Branch):
    def __init__(self, node_code, name, address, phone, client_id):
        super().__init__(node_code, name, address, phone)
        self.client_id = client_id

    def show_info(self):
        print(f"Client: {self.name}, Client ID: {self.client_id}")


class Account(Branch):
    def __init__(self, node_code, name, address, phone, account_number, balance):
        super().__init__(node_code, name, address, phone)
        self.account_number = account_number
        self.balance = balance

    def show_info(self):
        print(f"Account: {self.account_number}, Balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount


class Card(Account):
    def __init__(self, node_code, name, address, phone, account_number, balance, card_number):
        super().__init__(node_code, name, address, phone, account_number, balance)
        self.card_number = card_number

    def show_info(self):
        print(f"Card: {self.card_number}, Associated with Account: {self.account_number}")

    def make_payment(self, amount):
        if amount <= self.balance:
            self.balance -= amount


# Create objects of each class and test methods
branch = Branch("B1", "Mercedes", "123 Main St", "555-1234")
branch.create()
branch.delete()

employee = Employee("B2", "John Smith", "456 Elm St", "555-5678", "E101", "Manager")
employee.show_info()
employee.change_position("Assistant Manager")
print(f"New Position: {employee.position}")

client = Client("B3", "Mary Johnson", "789 Oak St", "555-9876", "C201")
client.show_info()

account = Account("B4", "Savings Account", "101 Pine St", "555-4321", "12345678", 1000.0)
account.show_info()
account.deposit(500)
account.withdraw(200)
print(f"Balance after transactions: {account.balance}")

card = Card("B5", "Credit Card", "101 Pine St", "555-4321", "87654321", 500.0, "T1001")
card.show_info()
card.make_payment(300)
print(f"Balance of the account associated with the card: {card.balance}")
