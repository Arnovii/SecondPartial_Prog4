import Classes as cls
import functions as fnc


def main():
    IDlIST = [] # List of all IDs of the vehicle. Used to check if the ID is already in use
    vehiclesList = [] # List of all vehicles that have been saved to the file Vehicles.txt. Used to save the information of the vehicles in the file

    if vehiclesList == []: # If the list is empty, then the information of the file Vehicles.txt is erased
        with open(cls.fileTextPath, "w") as file:
            file.write("")

    option = fnc.select_another_option()

    print(f"The option is: {option}")

    while option != 0:
        match option:
            case 1:
                pass
                option = fnc.select_another_option()
            case 2: 
                pass 
                option = fnc.select_another_option()

            case 3: 
                pass 
                option = fnc.select_another_option()
            
            case 4:
                pass 
                option = fnc.select_another_option()

            case 5:
                pass 
                option = fnc.select_another_option()
                
            case _:
                print("ERROR. The user input is not valid...")
                option =  fnc.select_another_option()

    print("\nThanks for using the system.\n")


main()