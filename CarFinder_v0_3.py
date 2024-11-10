#CarFinder
#This version allows the sales manager to add items to vehicles list.

AllowedVehiclesList = ['Ford F-150' , 'Chevrolet Silverado' , 'Tesla Cybertruck' , 'Toyota Tundra' , 'Nissan Titan']

#Adding the menu.
def print_menu():
    print('********************************')
    print('AutoCountry Vehicle Finder v0.3')
    print('********************************')
    print('Please Enter the following number below from the following menu:')
    print('1. PRINT all Authorized Vehicles')
    print('2. SEARCH for Authorized Vehicle')
    print('3. ADD Authorized Vehicle')
    print('4. Exit')
    print('********************************')

#Adding the end part of the menu.
def print_all_vehicles():
    print('Authorized Vehicles:')
    for vehicle in AllowedVehiclesList:
        print(vehicle)
        print('*******************************')

#Defining search option.
def search_vehicle(vehicle_name):
    if vehicle_name in AllowedVehiclesList:
     print(f"{vehicle_name} is an authorized vehicle")
    else:
        print(f"{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again")
        print('********************************')



#Second part of the menu 
def print_allowed_vehicles_list():
    print('\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
    for vehicles in AllowedVehiclesList:
        print(vehicles)
    menu = f"""
The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:
{print_allowed_vehicles_list}
*******************************
AutoCountry Vehicle Finder v0.2
*******************************
Please Enter the following number below from the following menu:
1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. Exit
"""
#
def main():
    while True:
        print_menu()
        option = input()
        if option == '1':
            print_allowed_vehicles_list()
        elif option == '2':
            vehicle_name = input('Please Enter the full vehicle name:')
            search_vehicle(vehicle_name)
        elif option == '3':
            print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
            break
        else:
            print('Invalid option. Please try again.')

if __name__ == '__main__':
    main()