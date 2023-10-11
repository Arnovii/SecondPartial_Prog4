import Classes as cls
import functions as fnc

def main():
    if fnc.vehiclesList == []: # If the list is empty, then the information of the file Vehicles.txt is erased
        with open(cls.fileTextPath, "w") as file:
            file.write("")
            print("The information of the file Vehicles.txt has been erased.\n")

    option = fnc.select_another_option()

    while option != 0:
        match option:
            case 1:
                fnc.create_vehicle()
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