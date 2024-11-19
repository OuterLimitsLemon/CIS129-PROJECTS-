#Oscar E. Saenz
#Professor Troy Adams
#CIS129
#Module 11: 9.2 "Class Average: Reading Grades from a Plain Text File"

#display_grades() function: Displays list of all grades input
def display_grades():
    with open('grades.txt', mode='r') as students:
        for grade in students:
            print(f'{grade.strip()}')

#average_from_txt() function: Calculated and displays average from txt file
def average_from_txt():
    display = []
    display2 = []
    denominator = 0
    numerator = 0
    average = 0
    with open('grades.txt', mode='r') as students:
        for grade in students:
            display.append(grade.strip())
        del display[0]
        for num in display:
            num_1 = float(num)
            display2.append(num_1)
        denominator = len(display2)
        for num2 in display2:
            numerator += num2
        average = numerator / denominator
        print(f'{average:.2f}')
        
        
#Calls average_from_txt() & display_grades()
print("\n___________________________________________________________")
display_grades()
print()
print("The class average is approximately:")    
average_from_txt()
print()
print("*Rounded to nearest hundreth.")
print("___________________________________________________________")

