#Oscar E. Saenz
#Professor Troy Adams
#CIS129
#7 October 2024

#CIS129_OscarSaenz_Lab5.py
#Objective: Build a program which tracks bottles collected by a grocer over a week.
#The program will allow the user to input bottles collected.
#The program will display for the user total bottles collected and total payout.
#The store pay's out $0.10 per bottle. 


#Initialize Variables 


# totalBottles: This variable will store the total bottles collected
totalBottles = 0

# counter: This variable will control the loop
counter = 1

# todayBottles: This variable will store the number of bottles returned on a day
todayBottles = 0

# totalPayout: This variable will store the calculated value of totalBottles times 0.10
totalPayout = 0

# keepGoing: A variable initialized to "y"
keepGoing = "y"

#This imports the Decimal type used for the calculations
from decimal import Decimal


#Processing & Terminating 


#The below code contains a number of components. Here is a breakdown of the heirarchy.  
#1. The code begins with some visual formatting. 
#2. The loop is built about a 'while' control statement which continues to loop as long as keepGoing is equal to "y."
#3. The next component requests the user to enter the number of bottles they collected while simultaniously keeping track of the number of user inputs (counter).
#4. The number of bottles entered by the user generates a value for todayBottles.
#5. todayBottles is used to generate the final displayed total bottles and payout (generates values for variables: totalBottles, totalPayout)
#6. When the user has entered an input 7 times, the program will display totals and ask if the user wishes to use the program again.
#7. If the user enter's "y" for "yes," the program will start over - indefinetly. 
#8. If the user enter's "n" for "no," the program will terminate. 

while keepGoing == "y":
   for counter in range(1,8):
        todayBottles = int(input(f'Enter number of bottles for day #{counter}: '))
        totalBottles += todayBottles 
        totalPayout = totalBottles * Decimal('.10')
        if counter == 7:
            print(f'\nThe total number of bottles is {totalBottles}')
            print(f'The total paid out is ${totalPayout}\n')
            if input("Do you want to enter another week's worth of data? \n(Enter y or n): ") == "y":
                print()
                totalBottles = 0
                todayBottles = 0
                totalPayout = 0
                keepGoing = "y"
            else: 
                keepGoing = "n"
                

#The program concludes with some basic visual formatting. 
print('>>>')