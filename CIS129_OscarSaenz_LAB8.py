#Oscar E. Saenz
#Professor Troy Adams 
#CIS129
#27 October 2024

#Module 8: 'Palindrome Tester'
#Confirms if a word entered is a 'Palindrome' or not! 


#Functions


#Sanitizes user input: checks for numbers, special characters, spaces and blank entries
#Also confirms user input is greater than 2 letters
def sanitized():
    """ Sanitizes user input """
    while True:
        sanitized = []
        space_counter = 0
        numerical_counter = 0
        special_character_counter = 0
        not_sanitized = list(input("\n\nPlease enter a word: ").upper())
        
        #Warns user of blank entry.
        if not not_sanitized:
            print("Blank entry.\n")
            continue
        
        #Warns user of space
        for test in not_sanitized:
            if test == ' ':
                space_counter += 1
            else:
                try:
                    
                    #Filters numerical inputs
                    int(test)
                    numerical_counter += 1
                except ValueError:
                    
                    #Filters special characters
                    special_characters = [
                        "", "~", "@", "#", "$", "%", "^", "&", "*", "(", ")", 
                        "-", "_", "=", "+", "[", "{", "]", "}", ":", "|", ";", 
                        "'", ",", "<", ".", ">", "/", "?"]
                    if test in special_characters:
                        special_character_counter += 1
                        break
                    
                    #Builds a list of sanitized inputs
                    else:
                        sanitized.append(test)
                        
        #Confirms length of input is greater than 2 letters               
        if space_counter > 0:
            print("Please do not leave blank spaces.\n")
            continue
        if numerical_counter > 0:
            print("Please do not enter numerical values.\n")
            continue
        if special_character_counter > 0:
            print("Please do not enter any special characters.\n")
            continue
        if len(sanitized) < 3:
            print("Your word must have more than 2 letters.\n")
            continue
        return sanitized
             
#Provides number of elements in list generated from user input. Used to text word length.
def length_tester(sanitized):
    """ Gives number of elements in a list """
    return len(sanitized) 

#Makes a sopy of the users sanitized input and rearranges it from right-to-left 
def reverser(sanitized_entry):
    """ Rearranges list from right to left """
    sanitized_entry2 = sanitized_entry.copy()
    sanitized_entry2.reverse()
    return sanitized_entry2

#Tests if the user input is a palindrome or not.
def palindrome_tester(sanitized_entry, right_to_left):
    """ Tests if list is a palindrome or not (only works on letters) """
    print('Forwards: ',sanitized_entry)
    print('Reversed: ',right_to_left)
    master_list = []
    master_list = zip(sanitized_entry, right_to_left)
    for sanitized_entry, right_to_left in master_list:
        if sanitized_entry != right_to_left:
            print("\nYour word failed the palindrome test.\n")
            return
    print("\nYour word passed the palindrome test!\n")

#Would you like to try again? 
def try_again():
    """ Confirms with user if they want to try again """
    print()
    while True:
        response = input("\nWould you like to try again? (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            return 'true'
        elif response in ['n', 'no']:
            return 'end'
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.\n")


#Initialize Global Variables

#Controls the "Press any key to continue... " condition
any_input = ''

#Maintains the 'while' loop until user chooses to end program.        
yes_or_no = 'true'

print()
print("From the studio that brought you beloved classics such as:")
print("  - 'Theater Seating Lab,'")
print("  - 'Repitition Structures'")
print("  - 'Hotdog Cookout Lab'\n\n\n")
any_input = input("Press any key, then 'ENTER' to continue... ")

if any_input != '':
    print("\n\n-------------------------------------------------------\n")
    print()
    print("             Welcome to Palindrome Tester!")
    print("                      By O-Tech\n\n")
    print("pal·in·drome, noun\n       a word that reads the same backward as forward.")
#While loop used to keep the program looping until stopped by user.
    while yes_or_no == 'true':

        print("-------------------------------------------------------")    
        sanitized_entry = sanitized()
        right_to_left = reverser(sanitized_entry)
        palindrome_tester(sanitized_entry, right_to_left)
        yes_or_no = try_again()
        print("-------------------------------------------------------\n")

    print()
    print("Goodbye!")
    print()
    print("Palindrome Tester 2.1.3 *All Rights Reserved")
    print("PPi:1-a 2024")

