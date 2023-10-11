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
    print("2. Search and show the information of a vehicle")
    print("3. Modify a vehicle")
    print("4. Show all vehicles information")
    print("5. Update the information of the file Vehicles.txt")
    print("6. Convert miles to kilometers")
    
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

def modify_vehicle():
    print("\n\tMODIFYING A VEHICLE...\n")
    vehicle = search_vehicle_by_ID()
    if vehicle:
        print(vehicle) # The information of the vehicle is shown
        print("1. Modify the brand")
        print("2. Modify the model")
        print("3. Modify the year")
        print("0. Exit")
        option = input("\nPlease select an option: ")
        if option.isdigit():
            option = int(option)
            if option == 1:
                brand = input("Please enter the new brand of the vehicle: ")
                vehicle.set_brand(brand)
                print("\nBrand modified successfully.\n")
            elif option == 2:
                model = input("Please enter the new model of the vehicle: ")
                vehicle.set_model(model)
                print("\nModel modified successfully.\n")
            elif option == 3:
                year = input("Please enter the new year of the vehicle: ")
                vehicle.set_year(year)
                print("\nYear modified successfully.\n")
            elif option == 0:
                pass
            else:
                print("ERROR. The user input is not valid...")
        else:
            print("ERROR. The user input is not valid...")
    else:
        print("The vehicle was not found...")

def show_all_vehicles_information():
    print("\n\tSHOWING ALL VEHICLES INFORMATION...\n")
    for vehicle in vehiclesList:
        print(vehicle)

def save_all_vehicles_information_in_a_file():
    print("\n\tSAVING ALL VEHICLES INFORMATION IN A FILE...\n")
    with open(cls.fileTextPath, "w") as file:
        file.write("")
        for vehicle in vehiclesList:
            vehicle.save_info()
    print("Vehicles information has been updated successfully.\n")

def is_valid_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def convert_miles_to_kilometers():
    print("\n\tCONVERTING MILES TO KILOMETERS...\n")
    miles = input("Please enter the miles: ")
    while not is_valid_float(miles):
        print("ERROR. The user input is not a valid float...")
        miles = input("Please enter the miles: ")
    miles = float(miles)
    converter = cls.Converter(miles)
    message = f"{converter.get_miles()} miles = {converter.get_kilometers()} kilometers"
    print(message)
    with open(cls.fileTextConverterPath, "a") as file:
        file.write(message + "\n")

