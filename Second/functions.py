import Classes as cls

IDlIST = [] # List of all IDs of the vehicle. Used to check if the ID is already in use
vehiclesList = [] # List of all vehicles that have been saved to the file Vehicles.txt. Used to save the information of the vehicles in the file


def validate_ID(ID): # Function that validates if the ID is already in use
    if ID in IDlIST:
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
    print("6. Save all vehicles information in a file")
    print("7. Convert miles to kilometers")
    
    print("\n0. Exit")

def select_another_option():
    input("\nPress Enter to continue...")
    cls.os.system('cls')
    print_menu_information()
    userAnswer = input("\nPlease select an option: ")
    if userAnswer.isdigit():
        userAnswer = int(userAnswer)
    return userAnswer

def create_vehicle():
    print("\n\tCREATING A NEW VEHICLE...\n")
    vehicleID = input("Please enter the ID of the vehicle: ")
    while not validate_ID(vehicleID):
        print("ERROR. The ID is already in use. Please enter another ID.")
        vehicleID = input("Please enter the ID of the vehicle: ")
    IDlIST.append(vehicleID)

    brand = input("Please enter the brand of the vehicle: ")
    model = input("Please enter the model of the vehicle: ")
    year = input("Please enter the year of the vehicle: ")

    vehicle = cls.Vehicle(vehicleID, brand, model, year)
    vehiclesList.append(vehicle)
    print("\nVehicle created successfully.\n")


def search_vehicle_by_ID():
    print("\n\tSEARCHING A VEHICLE...\n")
    vehicleID = input("Please enter the ID of the vehicle: ")

    for vehicle in vehiclesList:
        if vehicle.get_vehicleID() == vehicleID:
            return vehicle
    
    return None # If the vehicle is not found, then the function returns None