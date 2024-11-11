#Oscar E. Saenz
#Professor Troy Adams
#CIS129
#10 November 2024

#Initialize variables
yes_or_no = 'true'
sanitized_input = []

#Function Definitions

#Asks the user to input a number - warns the user if a bad input was entered. 
def sanitized():
    """ Sanitizes user input for spaces, special symbols, numbers than $999,999.99 and letters """
    while True:
      special_character_counter = 0 
      blank_space_counter = 0
      sanitized_test = []
      ready_for_decimal_test = ''
      not_sanitized = []
      not_sanitized = list(input("\n\nPlease enter dollar amount: $"))
      
      #Warns user if nothing was entered and starts the loop over. 
      if not_sanitized == []:
           print("Please do not leave blank.\n")
           continue
       
      #Confirms if the input is either a numerical or decimal point
      for test in not_sanitized:
          try:
              float(test)
              sanitized_test.append(test)
          except ValueError:
              special_characters = [
                        "", "~", "@", "#", "$", "%", "^", "&", "*", "(", ")", 
                        "-", "_", "=", "+", "[", "{", "]", "}", ":", "|", ";", 
                        "'", ",", "<", ">", "/", "?"]
              if test in special_characters:
                  special_character_counter += 1
                  break
              elif test == ' ':
                  blank_space_counter += 1
              elif test.isalpha() == True:
                      special_character_counter += 1
                      break
              else: 
                  sanitized_test.append(test)
                  
     #Warns the user if a bad input was entered and starts the loop over.   
      if special_character_counter > 0:
          print("Please only enter numerical values and/or a decimal point.\n")
          continue
      
      #Warns the user if an empty space was entered and starts the loop over.  
      if blank_space_counter > 0:
          print("Please do not leave blank spaces.\n")
          continue
      
      #Warns the user if more than one decimal point was entered and starts the loop over.
      ready_for_decimal_test = ''.join(sanitized_test.copy())
      if ready_for_decimal_test.count('.') > 1:
          print("Please only enter a single decimal point.")
          continue
      
        #Warns the user that their input must be less than or equal to $999,999.99
      if float(ready_for_decimal_test) > 999999.99:
          print("This program does not allow values greater than $999,999.99.")
      else:
          return float(ready_for_decimal_test)     

#Prints the sanitized format to $*******0.00 format
def check_protector(sanitized_input):
    """ Formats the input to $*******0.00 format. Also rounds down to nearest .01 """
    decimal_formated = ((sanitized_input * 100) // 1) * .01
    return print(f'${decimal_formated:*>10,.2f}')

#Would you like to enter another input? 
def try_again():
    """ Confirms with user if they want run the program again """
    print()
    while True:
        response = input("\nWould you like to enter another input? (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            return 'true'
        elif response in ['n', 'no']:
            return 'end'
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.\n")

#Calls
print()
print(f'{"Check Protector":^68}')
print("This program allows up to $999,999.99 - including one decimal point.")
print(f'{"Do not use a comma.":^68}')
print("--------------------------------------------------------------------")
print()

#Controls the try_again() function which confirms if the user wants to run the program again 
while yes_or_no == 'true':
    
    #Calls the sanitized() function 
    sanitized_input = sanitized()  
    
    #Calls the check_protector() function 
    check_protector(sanitized_input)
    
    #Calls the try_again() function
    yes_or_no = try_again()
    print("-----------------------------------------------")
print("\n\nEnd of Program.")
