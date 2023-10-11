import os

def validate_ID(ID, list): # Function that validates if the ID is already in use
    if ID in list:
        return False
    else:
        return True
    
def print_menu_information():
    print("\n\nWELCOME TO THE VEHICLE MANAGER\n")

    print("1. Create a new vehicle")
    print("2. Search a vehicle")
    print("3. Show vehicle information")
    print("4. Modify a vehicle")
    print("5. Show all vehicles")

    print("\n0. Exit")

def select_another_option():
    input("\nPress Enter to continue...")
    os.system('cls')
    print_menu_information()
    userAnswer = input("\nPlease select an option: ")
    if userAnswer.isdigit():
        userAnswer = int(userAnswer)
    return userAnswer
