#Oscar E. Saenz
#Professor Troy Adams
#CIS129
#19 October 2024

#Lab 7: "Theater Seating Lab"

#initialization
userTitle = ''
quantity_of_sections = 0
sectionTitles = []


#eventTitle Function: Requests an event name from the user. The user may forego this if desired.
def eventTitle(userTitle):
    """Requests an event name from the user. The user may forego this if desired. """
    yes_or_no1 = ''
    while yes_or_no1 != 'y' and yes_or_no1 != 'n':

        #Asks the user if they would like to title their event (y/n)
        yes_or_no1 = input("Would you like to name your event (y/n)? ").lower()
        if yes_or_no1 == "y": 
            userTitle = input("Please enter event title: ").title()
            yes_or_no2 = ''
            while yes_or_no2 != 'y' and yes_or_no2 != 'n':

                #Confirms the title with the user - the user can rewrite their original input if desired.
                yes_or_no2 = input(f"\nYou have titled your event '{userTitle}' \nWould you like to proceed with this title (y/n)? ")
                if yes_or_no2 == "y":
                    return userTitle
                elif yes_or_no2 == "n": 
                    print()
                    yes_or_no1 = ''

                #Reminds the user to only enter 'y' or 'n'. Blank spaces or additional characters are not accepted.
                else: 
                    print("Please enter either 'y' or 'n'.\n")

        #"Untitled Event" if user chooses not to assign a title
        elif yes_or_no1 == 'n':
            userTitle = "Untitled Event"
            return userTitle

        #Reminds the user to only enter 'y' or 'n'. Blank spaces or additional characters are not accepted.
        else:
            print("Please enter either 'y' or 'n'.\n")


#sectionsQuantity Fuction: Requests the number of seating sections from the user.
def sectionsQuantity(quantity_of_sections):
    """ Requests number of seating sections from user """
    while quantity_of_sections == 0:

        #Asks the user to enter a quantity for the number of sections. 
        userInput = input("Enter number of seating sections: ")

        #Warns the user not to leave the input blank.
        if userInput == "":
            print("Please, do not leave blank.")

        #Confirms a correct value has been input.
        else:
            try:
                quantity_of_sections = int(userInput)

                #Confirms the input is greater than 0.
                if quantity_of_sections > 0:
                    yes_or_no3 = ''
                    while yes_or_no3 != 'y' and yes_or_no3 != 'n':

                        #Confirms the number of sections entered with the user. 
                        yes_or_no3 = input(f"There are {quantity_of_sections} sections. Is this correct (y/n)? ")
                        if yes_or_no3 == 'y':
                            print()
                        elif yes_or_no3 == 'n':
                            quantity_of_sections = 0
                            print()

                        #Reminds the user to only enter 'y' or 'n'. Blank spaces or additional characters are not accepted.
                        else:
                            print("Please enter either 'y' or 'n'.\n")

                #Reminds the user to only enter a value greater than 0.
                else:
                    quantity_of_sections = 0
                    print("Please enter a number greater than 0.\n")

            #Warns the user if an invalid input is entered. 
            except ValueError:
                print("Invalid input. Please enter only numerical inputs greater than 0.\n")

    return quantity_of_sections

#sectionTitle Function: Asks the user to title their sections. 
def sectionTitle():
    """ Asks the user to title their sections. """
    yes_or_no4 = ''
    while yes_or_no4 != 'y' and yes_or_no4 != 'n':
        for sectionTitleQuant in range(1, quantity_of_sections + 1):
            titles = input(f"Please title section {sectionTitleQuant}: ").title()
            sectionTitles.append(titles)
            
        #Confirms inputs with user - resets if user indicates it is  incorrect. 
        yes_or_no4 = input(f"You have named your section(s) {sectionTitles}. Is this correct (y/n)? ")
        if yes_or_no4 == 'y':
            print()
        elif yes_or_no4 == 'n':
                yes_or_no4 = ''
        else: 
            print("Please enter either 'y' or 'n'.\n")
    return sectionTitles


#Call to request event title "eventTitle"
print("_________________________________________________________________\n")
eventTitle(userTitle)

#Call to requst number of seating sections from the user "sectionsQuantity"
print("_________________________________________________________________\n")
quantity_of_sections = sectionsQuantity(quantity_of_sections)

#Call to request a title for each section "sectionTitle"
print("_________________________________________________________________\n")
sectionTitles = sectionTitle()

