#Oscar E. Saenz
#Professor Troy Adams
#CIS129
#24 November 2024
#Module 12: Class 'Pet' 
#Description: Creates a class named 'Pet' which contains pet name, pet type and pet age

# Class Definition

# "Pet" class definition contains pet name, pet type and pet age
class Pet: 
    """ Sets class 'Pet' which contains pet name, type and age! """
    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age
    
    # Allows for 'name' attribute to be adjusted to given value
    def setName(self, name):
        self.name = name 
        return
    
    # Allows for 'type' attribute to be adjusted to given value
    def setType(self, type):
        self.type = type
        return
    
    # Allows for 'age' attribute to be adjusted to given value
    def setAge(self, age):
        self.age = age
        return
    
    # Returns the value of the 'name' attribute
    def getName(self):
        return self.name
    
    # Returns the value of the 'type' attribute
    def getType(self):
        return self.type
    
    # Returns the value of the 'age' attribute
    def getAge(self):
        return self.age

# Function definition

# your_pet function: requests user input needed to set user_pet(name, type, age)
def your_pet():
    """ Creates object fro user input pet name, type and age! """
    # Imports 'string' module needed for punctuation test (further down)
    import string
    
    # Initialized name, type, age variables to empty - pending input from user
    user_pet_name = ''
    user_pet_type = ''
    user_pet_age = None   
    
    # Requests user to input pet name. Removes empty whitespace, capitalizes inputs and repeats if blank. Allows for numbers and punctuation.
    while user_pet_name == '': 
        user_pet_name = input('\nPlease enter the name of your pet: ').strip().capitalize()
    
    # Requests user to input pet type. Removes empty whitespace, capitalizes inputs and repeats if blank. Does not allow for numbers and punctuation. 
    while user_pet_type == '':
        user_pet_type = input('Please enter your pet type (i.e. "Dog", "Cat"...): ').strip().capitalize()
        
        # Tests for punctuation and/or numbers in the pet type input. 
        test = list(user_pet_type)
        test_failed = []
        for i in test:
            if i in string.punctuation:
                test_failed.append("Failed")
        for i in test: 
            try:
                int(i)
                test_failed.append("Failed")
            except ValueError: 
                continue 
        
        # Displays error message to user if numbers or punctuation is input for the pet type. 
        if "Failed" in test_failed:
            print("Please do not use punctuation or numerical characters.\n")
            test_failed = []
            user_pet_type = ''
                
    # Requests user to input pet age. Removes empty whitespace and repeats if blank. Letters and punctuation not allowed.
    while user_pet_age == None:
        
        # Confirms the input is a number. 
        try:
            user_pet_age = int(input('Please enter the age of your pet: ').strip())
            
            # Sets user_pet = sanitized inputs entered by user: name, type, age.
            user_pet = Pet(user_pet_name, user_pet_type, user_pet_age)
            
            # Displays all pet information - name, type and age. 
            print("-------------------------------------")
            print(f"Pet Name: {user_pet.getName()}")
            print(f"Pet Type: {user_pet.getType()}")
            print(f"Pet Age:  {user_pet.getAge()}")
            return user_pet
        
        # Blocks input to user_pet_age if user input is not a number.
        except ValueError: 
            print("Please enter a (whole) number.\n")

# Call(s)

# Call to run your_pet()            
user_pet = your_pet()
    
    
    
    
    
    