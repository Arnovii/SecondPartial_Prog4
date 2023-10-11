class Branch:
    def __init__(self, node_code, name, address, phone):
        self.node_code = node_code
        self.name = name
        self.address = address
        self.phone = phone

    def create(self):
        with open('Branches.txt', 'a') as file:
            file.write(f"Branch: {self.name}\n")
            file.write(f"Node Code: {self.node_code}\n")
            file.write(f"Address: {self.address}\n")
            file.write(f"Phone: {self.phone}\n")
            file.write(f" -----------------------------------------------------")
        print(f"Branch '{self.name}' created")

    def delete(self):
        with open('Branches.txt', 'r') as file:
            lines = file.readlines()

        branchStart = None
        branchEnd = None

        for i, line in enumerate(lines):
            if line.startswith("Branch: " + self.name):
                branchStart = i
                break

        if branchStart is not None:
            for i in range(branchStart, len(lines)):
                if lines[i].startswith(" -----------------------------------------------------"):
                    branchEnd = i
                    break

        if branchStart is not None and branchEnd is not None:
            del lines[branchStart:branchEnd + 1]

            with open('Branches.txt', 'w') as file:
                file.writelines(lines)
    
class Employee(Branch):
    def __init__(self, node_code, name, address, phone, employee_id, position):
        super().__init__(node_code, name, address, phone)
        self.employee_id = employee_id
        self.position = position

    def save_info(self):
        with open('Employees.txt', 'a') as file:
            file.write(f"Employee: {self.name}\n")
            file.write(f"Node Code: {self.node_code}\n")

    def change_position(self, new_position):
        self.position = new_position

class Client(Branch):
    def __init__(self, node_code, name, address, phone, client_id):
        super().__init__(node_code, name, address, phone)
        self.client_id = client_id

    def save_info(self):
        with open('Clients.txt', 'a') as file:
            file.write(f"Client: {self.name}\n")
            file.write(f"Node Code: {self.node_code}\n")

class Account(Branch):
    def __init__(self, node_code, name, address, phone, account_number, balance):
        super().__init__(node_code, name, address, phone)
        self.account_number = account_number
        self.balance = balance

    def save_info(self):
        with open('Accounts.txt', 'a') as file:
            file.write(f"Account number: {self.account_number}\n")
            file.write(f"Node Code: {self.node_code}\n")

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

class Card(Account):
    def __init__(self, node_code, name, address, phone, account_number, balance, card_number):
        super().__init__(node_code, name, address, phone, account_number, balance)
        self.card_number = card_number

    def save_info(self):
        with open('Cards.txt', 'a') as file:
            file.write(f"Card number: {self.card_number}\n")
            file.write(f"Node Code: {self.node_code}\n")

    def make_payment(self, amount):
        if amount <= self.balance:
            self.balance -= amount