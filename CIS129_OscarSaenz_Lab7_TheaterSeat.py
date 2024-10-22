#Oscar E. Saenz
#Professor Troy Adams
#CIS129
#21 October 2024
#Lab 7: "Theater Seating Lab"

def main():
    
    
    #Stored Constants: Section Names
    Section = ['A', 'B', 'C']

    #Stored Constants: Section Seating Quantities 
    Section_Seats = [300, 500, 200]

    #Stored Constants: Section Prices 
    Section_Pricing = [20, 15, 10]
    
    #Combines the values of the above 3 lists
    zipped_name_seats_prices = list(zip(Section, Section_Seats, Section_Pricing))
    
    #Keeps track of tickets sold
    Tickets_Sold_Total = [0] * len(Section)
    
    #Keeps track of total dollars
    Ticket_Revenue = 0
    
    #Keeps loop operating
    Transaction = 'y'
    
    #Optional employee name variable 
    name = ''
    
    #Welcome Message: Congrats, you are now an employee at The Dusty Theater! 
    print("-----------------------------------------")
    print("Welcome to The Dusty Theater!")
    print()
    print("Good evening, Team Member.")
    print("Your tasks for tonight are as follows:")
    print("   1. Provide customers with a subtotal for their ticket purchases.")
    print("   2. Monitor available seating in each section.")
    print("   3. Track the total revenue generated for the evening.")
    print()
    print("Here are the seating sections available tonight:")

    #Displays price and seating information
    for section, seat, price in zipped_name_seats_prices:
        print(f"Section {section} at ${price:.2f}")
    print("\n")
    
    #Uses the employeeName() function to request a name input from the employee
    name = employeeName()
    print("\n-----------------------------------------\n")
    
    #Begins the loop
    while Transaction in ['y', 'yes']:
        SubTotal = 0
        Tickets_Sold = []
        Tickets_Sold_Appended = []
        Tickets_Sold_x_Price = []
        Seats_Remaining = []
        Seats_Remaining_Section = []
        print()
        print("Welcome to The Dusty Theater!")
        print(f"Team Member: {name}")
        
        #Iterates through zipped_name_seats_prices and stores tickets sold inputs in Tickets_Sold_Appended
        for section, seat, price in zipped_name_seats_prices:
            print(f"Please input the number of tickets sold in Section {section} at ${price:.2f}: ", end="")
            Tickets_Sold = NumericalValidation("")
            Tickets_Sold_Appended.append(Tickets_Sold)
        
        #Multiplys price of tickets to tickets sold
        Tickets_Sold_x_Price = [sold * price for sold, price in zip(Tickets_Sold_Appended, Section_Pricing)]
        SubTotal = sum(Tickets_Sold_x_Price)
        
        #Generates total revenue 
        Ticket_Revenue += SubTotal
        
        #Update the running total of tickets sold for each section
        Tickets_Sold_Total = [total + sold for total, sold in zip(Tickets_Sold_Total, Tickets_Sold_Appended)]
        
        #Calculates remaining seats
        Seats_Remaining = [seats - sold for seats, sold in zip(Section_Seats, Tickets_Sold_Total)]
        Seats_Remaining_Section = list(zip(Section, Seats_Remaining))
        
        #Display seats, SubTotal, Total Revenue
        print()
        print(f"Seats Remaining by Section: {Seats_Remaining_Section}")
        
        print("-----------------------------------------")
        print(f"SubTotal: ${MonetaryConversion(SubTotal):.2f}")
        print(f"Total Sales: ${Ticket_Revenue:.2f}")
        
        #Asks the user if they would like to enter another trasnaction
        print("\n\nWould you like to enter another transaction (y/n)? ", end='')  
        Transaction = Yes_or_No("")
        print("-----------------------------------------")
        
#Asks for an employee name        
def employeeName():
    """Requests an employee from the user. The user may forego this if desired. """
    yes_or_no1 = ''
    while yes_or_no1 != 'y' and yes_or_no1 != 'n':

        #Asks the user if they would like to name themselves (y/n)
        yes_or_no1 = input("Would you like to begin with your name (y/n)? ").lower()
        if yes_or_no1 == "y": 
            userTitle = input("Please enter your name: ").title()
            yes_or_no2 = ''
            while yes_or_no2 != 'y' and yes_or_no2 != 'n':

                #Confirms the name with the user - the user can rewrite their original input if desired.
                yes_or_no2 = input(f"\nYou have named yourself '{userTitle}' \nWould you like to proceed with this name (y/n)? ")
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
            userTitle = "No Name!"
            return userTitle

        #Reminds the user to only enter 'y' or 'n'. Blank spaces or additional characters are not accepted.
        else:
            print("Please enter either 'y' or 'n'.\n")

#Validates numberical inputs - must be greater than or = to 0
def NumericalValidation(prompt):
    tickets_sold = ''
    while tickets_sold == '':
        tickets_sold = input()
        if tickets_sold == '':
            print(f"\nPlease do not leave blank.\n\nPlease input a valid number: ", end="")
        else: 
            try:
                int(tickets_sold)
                if int(tickets_sold) < 0:
                    print("\nPlease enter a quantity greater than or equal to zero.\n\nPlease input a valid number: ", end="")
                    tickets_sold = ''
                else:
                    validated_input = int(tickets_sold)
            except ValueError: 
                print("\nPlease enter only numerical inputs.\nSymbols and letters will not be accepted!\n\nPlease input a valid number: ", end="")
                tickets_sold= ''
    return validated_input

#Controls the while loop
def Yes_or_No(prompt):
    while True:  
        y_or_n1 = input(prompt).lower()  
        if y_or_n1 in ['y', 'yes', 'n', 'no']:
            return y_or_n1  
        else:
            print("\n\nInvalid input!\nPlease enter either 'y' or 'n': ", end="")
   
#Prints money values as 0.00 format
def MonetaryConversion(SubTotal):
    from decimal import Decimal
    return Decimal(SubTotal)
        

