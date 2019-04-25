# Brynne DuBois
# Professor Bui
# Hackers in the Bazaar
# Project 04

# Team Roster Management Tool
# Repurposed data structures project (C++ -> Python)

from functions import Athlete, displayRoster, addAthlete, deleteAthlete, editAthlete, saveFile, loadFile, nameChoice, positionChoice, numberChoice, heightChoice, weightChoice, hometownChoice, stateChoice, schoolChoice


menu_choice = 0
field_choice = 0
#roster_dict = dict()
   
while menu_choice != 8:
    print("\n\nWelcome to the Team Roster Management System!")
    print("********************Main Menu********************")
    print("1. Display the Team Roster")
    print("2. Add Athlete")
    print("3. Remove Athlete")
    print("4. Edit Athlete Info")
    print("5. Save Data")
    print("6. Load Data")
    print("7. Display Athlete by Data Field")
    print("8. Exit Program")
    menu_choice = int(input("Selection > "))

    if menu_choice == 1:
        displayRoster()
    elif menu_choice == 2:
        print("Please enter the following information for the new athlete:\n")
        first_last = input("Full Name: ")
        position = input("Position Played: ")
        number = input("Jersey Number: ")
        height = input("Height: ")
        weight = input("Weight: ")
        hometown = input("Hometown: ")
        home_state = input("State: ")
        school = input("High School: ")
        addAthlete(first_last, position, number, height, weight, hometown, home_state, school)
    elif menu_choice == 3:
        athlete_to_delete = input("Enter the name of the athlete to be removed: ")
        deleteAthlete(athlete_to_delete)
    elif menu_choice == 4:
        athlete_to_edit = input("Enter the name of the athlete you want to edit: ")
        editAthlete(athlete_to_edit)
    elif menu_choice == 5:
        file_name = input("What file do you want to save? ")
        output = open(file_name, "w")
        saveFile(file_name, output)
    elif menu_choice == 6:
        file_name = input("What file do you want to load? ")
        input_file = open(file_name, "r")
        loadFile(file_name, input_file)
    elif menu_choice == 7:
         print("Select a field to search by:")
         print("1. Full Name")
         print("2. Position")
         print("3. Number")
         print("4. Height")
         print("5. Weight")
         print("6. Hometown")
         print("7. State")
         print("8. High School")
         print("9. Go back to main menu")
         field_choice = int(input("Enter the field you would like to search: "))
         if field_choice == 1:
             name_choice = input("Enter the name you would like to search: ")
             nameChoice(name_choice)
         elif field_choice == 2:
             position_choice = input("Enter the position you would like to search: ")
             positionChoice(position_choice)
         elif field_choice == 3:
             number_choice = input("Enter the number you would like to search: ")
             numberChoice(number_choice)
         elif field_choice == 4:
             height_choice = input("Enter the height you would like to seach: ")
             heightChoice(height_choice)
         elif field_choice == 5:
             weight_choice = input("Enter the weight you would like to search: ")
             weightChoice(weight_choice)
         elif field_choice == 6:
             hometown_choice = input("Enter the hometown you would like to search: ")
             hometownChoice(hometown_choice)
         elif field_choice == 7:
             state_choice = input("Enter the state you would like to search: ")
             stateChoice(state_choice)
         elif field_choice == 8:
             school_choice = input("Enter the high school you would like to search: ")
             schoolChoice(school_choice)
    elif menu_choice == 8:
        print("Exiting program.")
    else:
        print("Invalid menu choice. Please enter a valid option.")
