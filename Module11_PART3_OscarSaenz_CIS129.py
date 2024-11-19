#Oscar E. Saenz
#Professor Troy Adams
#CIS129
#Module 11: 9.3 "Writing Student Records to a CSV File"

import csv

#records() function: gets information from user for storge in CSV file
def records():
    with open('grades.csv', mode='w', newline='') as student_grades:
        writer = csv.writer(student_grades)
        writer.writerow(['First Name', 'Last Name', 'Exam 1 Grade', 'Exam 2 Grade', 'Exam 3 Grade'])

        while True:
            # Get student info from the user
            first_name = input("Enter student's first name (or 'x' to quit): ").strip()
            if first_name.lower() == 'x':
                break
            last_name = input("Enter student's last name: ").strip()
            exam1 = input("Enter grade for exam 1: ").strip()
            
            #Displays error if bad input from user!
            try:
                float(exam1)
            except ValueError:
                print("Please enter a numerical input!\n")
                continue 
            exam2 = input("Enter grade for exam 2: ").strip()
            
            #Displays error if bad input from user!
            try:
                float(exam2)
            except ValueError:
                print("Please enter a numerical input!\n")
                continue 
            exam3 = input("Enter grade for exam 3: ").strip()
            
            #Displays error if bad input from user!
            try:
                float(exam3)
            except ValueError:
                print("Please enter a numerical input!\n")
                continue 

            # Write the students information as a row in the file
            writer.writerow([first_name.title(), last_name.title(), exam1, exam2, exam3])
            print(f"\nStudent record {first_name} {last_name} added to file!\n")

#display() function: Displays entered records
def display():
    print("You have entered the following records: ")
    with open('grades.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader) 
        
        # Display entered records
        for row in reader:
            print(row)
    print()

print("\n___________________________________________________________")
records()
display()





    