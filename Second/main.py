import Classes as cls

IDlIST = [] # List of all IDs of the vehicle. Used to check if the ID is already in use
vehiclesList = [] # List of all vehicles that have been saved to the file Vehicles.txt. Used to save the information of the vehicles in the file

if vehiclesList == []: # If the list is empty, then the information of the file Vehicles.txt is erased
    with open(cls.fileTextPath, "w") as file:
        file.write("")

def validateID(ID): # Function that validates if the ID is already in use
    if ID in IDlIST:
        return False
    else:
        return True
    

