#Oscar E. Saenz
#Professor Troy Adams
#CIS129
# 14 October 2024

#Module 6: Lab "Hotdog Cookout"
#This module is intended to help the user plan for their cookout.
#It will tell the user how many packages of hotdogs and buns to purchase depending on the number of guests attending.
#The module assumes each guest will consume 1 hotdog (with bun).


#Initialization


#Number of guests in attendance>
guests = 0

#Name of event
name_of_event = ''
yes_or_no = ''

#Number of hotdogs per guest
hot_dogs_per_guest = 0

#Total hotdogs needed
total_dogs = 0

#Asks the user for the name of their event
while yes_or_no != 'y' and yes_or_no != 'n':
    yes_or_no = input("\nWould you like to title your event? y/n: ")
    if yes_or_no == 'y':
        name_of_event = input("Please title your event: ")
    elif yes_or_no == 'n':
        name_of_event = "Untitled Event"
        print("Untitled Event")
    else:
        print("Please enter either 'y' or 'n'")

#Asks the user to enter the number of guests attending.
while guests == 0:
    user_input = input("Enter the number of guests attending your cookout: ")

    #Will warn user if blank space or invalid character is entered. 
    if user_input == "":
        print("Please do not leave blank.\n")
    else:
        try:
            guests = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")

#Asks the user to enter the number of hotdogs per guest.
while hot_dogs_per_guest == 0:
    user_input = input("Enter the number of hotdogs each guest will have: ")

    #Will warn user if blank space or invalid character is entered. 
    if user_input == "":
        print("Please do not leave blank.\n")
    else:
        try:
            hot_dogs_per_guest = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")


#Computation Phase: Provides the calculations needed for the final display. 


#Import 'math' needed for 'ceil' function in custom functions
import math 

#Hotdog buns come in packages of 8. Hotdogs come in packages of 10.

#Calculates the total number of hotdogs
total_dogs = guests * hot_dogs_per_guest

#Calculates the number of Hotdog packages needed
def number_of_hotdog_packages(total_dogs):
    """ Calculates the number of Hotdog packages needed """
    return math.ceil(total_dogs / 10)

#Calculates the number of Bun packages needed
def number_of_bun_packages(total_dogs):
    """ Calculates the number of Bun packages needed """
    return math.ceil(total_dogs / 8)

#Leftover Hotdogs
def remainder_hotdogs(total_dogs):
    """ Calculates the number of leftover hotdogs """
    return (10 * math.ceil(total_dogs / 10)) - total_dogs

#Leftover Buns
def remainder_buns(total_dogs):
    """ Calculates the number of leftover buns """
    return (8 * math.ceil(total_dogs / 8)) - total_dogs


#Display


#The module will also display the following information for the user: 

#Title of the event
print(f"\n\nTitle of Event: {name_of_event.title()}")

# 1. The minimum number of packages of hot dogs required.
print("Number of hotdog packages needed for guests: ", number_of_hotdog_packages(total_dogs))

# 2. The minimum number of packages of buns required.
print("Number of bun packages needed for guests: ", number_of_bun_packages(total_dogs))

# 3. The number of hot dogs that will be left over.
print("Leftover hotdogs: ", remainder_hotdogs(total_dogs))

# 4. The number of buns that will be left over.
print("Leftover buns: ", remainder_buns(total_dogs))
