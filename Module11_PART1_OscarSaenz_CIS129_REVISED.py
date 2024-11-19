#Oscar E. Saenz
#Professor Troy Adams
#CIS129
#Module 11: 9.1 "Class Average: Writing Grades to a Plain Text File"

def sanitized():
    """ Sanitizes the input to ensure valid grades. 'x' is sentinel value """
    
    program = ''
    final_list = []
    while program != 'fin':
        special_character_counter = 0
        blank_space_counter = 0
        sanitized_test = ''
        not_sanitized = ''
        
        # User input request
        not_sanitized = input('Enter student grades (Enter "x" to end program): ')
        
        # Accepts the sentinel value and closes out the program
        if not_sanitized == 'x':
            program = 'fin'
            break
        
        # Warns user if nothing was entered and starts the loop over.
        if not_sanitized.strip() == '':
            print("Please do not leave blank.\n")
            continue
        
        # Filters input allowing only numbers and sentinel value to be used by the function.
        try:
            float(not_sanitized)
            sanitized_test = not_sanitized
        except ValueError:
            special_characters = [
                "~", "@", "#", "$", "%", "^", "&", "*", "(", ")", 
                "-", "_", "=", "+", "[", "{", "]", "}", ":", "|", ";", 
                "'", ",", "<", ">", "/", "?"]
            if any(char in special_characters for char in not_sanitized):
                special_character_counter += 1
            elif ' ' in not_sanitized:
                blank_space_counter += 1
            else:
                special_character_counter += 1
        
        # Warns the user if a special character or letter (besides 'x') was entered and starts the loop over.
        if special_character_counter > 0:
            print('Please only enter numerical values and/or a decimal point.\n(Enter "x" to end program)\n')
            continue
        
        # Warns the user if an empty space was entered and starts the loop over.  
        if blank_space_counter > 0:
            print("Please do not leave blank spaces.\n")
            continue
        
        final_list.append(sanitized_test)
    
    # Writes sanitized inputs to txt file
    with open('grades.txt', mode='w') as grades:
        grades.write("Class Grades:\n")
        grades.write("\n".join(final_list))
    
    # Displays entered grades for user
    print("\n___________________________________________________________")
    print("You have entered the following grades: ")
    for grade in final_list:
        print(f"Entry: {grade}")
    print("\nPlease open 'grades.txt' to view as a word document.")

print("\n")

# Calls sanitized() which performs "Writing Grades to a Plain Text File"         
sanitized()
