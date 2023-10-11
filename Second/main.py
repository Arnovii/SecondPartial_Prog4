import Classes as cls
import functions as fnc

def main():
    option = fnc.select_another_option()

    while option != 0:
        match option:
            case 1:
                fnc.create_vehicle()
                option = fnc.select_another_option()
            case 2: 
                vehicle = fnc.search_vehicle_by_ID()    
                if vehicle:
                    print(vehicle)
                else:
                    print("The vehicle was not found...")
                option = fnc.select_another_option()

            case 3: 
                fnc.modify_vehicle()
                option = fnc.select_another_option()
            
            case 4:
                fnc.show_all_vehicles_information()
                option = fnc.select_another_option()

            case 5:
                fnc.save_all_vehicles_information_in_a_file()
                option = fnc.select_another_option()

            case 6:
                fnc.convert_miles_to_kilometers()
                option = fnc.select_another_option()
            case _:
                print("ERROR. The user input is not valid...")
                option =  fnc.select_another_option()

    print("\nThanks for using the system.\n")


main()