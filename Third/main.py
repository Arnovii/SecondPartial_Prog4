from classes import *

# Create objects of each class and test methods
branch = Branch("B1", "Mercedes", "123 Main St", "555-1234")
branch.create()
branch.delete()
branch.create()

employee = Employee("B2", "John Smith", "456 Elm St", "555-5678", "E101", "Manager")
employee.save_info()
employee.change_position("Assistant Manager")
print(f"New Position: {employee.position}")

client = Client("B3", "Mary Johnson", "789 Oak St", "555-9876", "C201")
client.save_info()

account = Account("B4", "Savings Account", "101 Pine St", "555-4321", "12345678", 1000.0)
account.save_info()
account.deposit(500)
account.withdraw(200)
print(f"Balance after transactions: {account.balance}")

card = Card("B5", "Credit Card", "101 Pine St", "555-4321", "87654321", 500.0, "T1001")
card.save_info()
card.make_payment(300)
print(f"Balance of the account associated with the card: {card.balance}")
