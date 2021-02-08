"""
Project Name: class-manager-project
Author: Serrano, Jahaziel A.
Description: create, read, update, delete your classes to be aware of your class calendar
"""

from manager import Class
import re
from sys import stdout
RED   = "\033[1;31m"
RESET = "\033[0;0m"
BLUE =  "\033[1;34m"


"""" check/verify data before inserting """
def insert(obj):
    # Validate input before insert
    obj.setClassName(validate('[a-zA-Z0-9]+', 'Insert a class: '))
    obj.setProfessor(validate('[a-zA-Z]+', 'Insert professor: '))
    obj.setDay(validate('[a-zA-Z]+', 'Insert class day: '))
    obj.setHour(validate('[0-9]{2}:[0-9]{2}-[0-9]{2}:[0-9]{2}', 'Insert class hours: '))
    obj.setSemesterYear(validate('[0-9]{4}-[0-9]{4}', 'Insert semester year: '))
    obj.setSemester(validate('(primero|segundo)', 'Insert semester: '))

    # Insert Data and return status
    status = obj.insert()

    # Show process status
    if status == 1:
        stdout.write(BLUE)
        print(f'\nSucessfully inserted data!')
        stdout.write(RESET)
    else:
        stdout.write(RED)
        print(f'\nValueError: Data Already Exists!')
        stdout.write(RESET)

    # Show Data
    obj.showData()

""" Delete a class/row """
def delete(obj):
    # Show classes/rows
    obj.showData()

    # Verify if the usar want to delete then delete class\row
    choose = input('Are you sure? All data with specify class name will be deleted\nEscribir (y|Yes|Y) si desea cotinuar: ')
    if choose.strip() in 'y,Y,yes,Yes,YES,yEs,yES,YeS'.split(','):
        obj.setClassName(validate('[a-zA-Z0-9]+', 'Insert a class: '))
        count_delete = obj.delete()
    print(f'Deleted: {count_delete}')

    # Show classes/rows
    obj.showData()

""" Modify specify data"""
def modify(obj):
    # show Data
    obj.showData()

    # Ask Options
    print('\nChoose between this option: ')
    print('1. class\n2. professor\n3. days\n4. hour\n5. year\n6. semester')
    choose = validate('([1-6])', 'Which type data you want to modify: ')

    # Send to the Class Manager

    if int(choose) < 6 and int(choose) > 0:
        if choose in 'classname,class,1'.split(','):
            new_data = validate('[a-zA-Z0-9]+', 'Insert new data: ')
            old_data = validate('[a-zA-Z0-9]+', 'Insert old data: ')
            status = obj.modify(0, new_data, old_data)
        elif choose in 'professor,2'.split(','):
            new_data = validate('[a-zA-Z0-9]+', 'Insert new data: ')
            old_data = validate('[a-zA-Z0-9]+', 'Insert old data: ')
            status = obj.modify(1, new_data, old_data)
        elif choose in 'days,day,3'.split(','):
            new_data = validate('[a-zA-Z0-9]+', 'Insert new data: ')
            old_data = validate('[a-zA-Z0-9]+', 'Insert old data: ')
            status = obj.modify(2, new_data, old_data)
        elif choose in 'hour,hours,4'.split(','):
            new_data = validate('[a-zA-Z0-9]+', 'Insert new data: ')
            old_data = validate('[a-zA-Z0-9]+', 'Insert old data: ')
            status = obj.modify(3, new_data, old_data)
        elif choose in 'semesteryear,semesteryears,5'.split(','):
            new_data = validate('[a-zA-Z0-9]+', 'Insert new data: ')
            old_data = validate('[a-zA-Z0-9]+', 'Insert old data: ')
            status = obj.modify(4, new_data, old_data)
        elif choose in 'semester,semesters,6'.split(','):
            new_data = validate('[a-zA-Z0-9]+', 'Insert new data: ')
            old_data = validate('[a-zA-Z0-9]+', 'Insert old data: ')
            status = obj.modify(5, new_data, old_data)
    else:
        old_data = choose + ' option'
        status = 0

    # Show process status
    if status == 0:
        stdout.write(RED)
        print(f"\n{old_data} not found or doesn't exist")
        {stdout.write(RESET)}
    else:
        stdout.write(BLUE)
        print(f"\nSucessfully moified data!")
        stdout.write(RESET)

    # showData
    obj.showData()

""" Remove spaces and validate data"""
def validate(pattern, massage):
    data = None
    while data is None:
        data = input(massage)
        data = list(data)
        for char in data:
            if char == ' ':
                data.remove(char)
        data = ''.join(data)
        if re.search(pattern, data):
            return data.lower().strip()
        else:
            sys.stdout.write(RED)
            print(f"\tValueError: {data} format violated!\n\tFormat: {pattern} ")
            sys.stdout.write(RESET)
            data = None


""" Show option panel """
def print_option():
    print(f"""
Class Manager System
Programmer: Serrano Bermudez, Jahaziel A.
by Kubik
===============================================
           Choose between 1-4:
               1. Insert
               2. modify
               3. Delete
               4. show
               5. End Program
===============================================
   -Class Manager organiza tus clases- 
   Si no ingresa un file este guardara
    los datos/cambios en classDB.csv     
===============================================""")

def main():

    """ Show options panel """
    print_option()

    # Start console app
    while True:
        # ClassManager Object
        class_data = Class()
        operator = input('\n>> ')

        # Option 1: Insert a new class/row
        if operator == '1':
            """ check data and then insert it"""
            insert(class_data)
            print('\nProcess ends\n')

        # Option 2: Modify a column of a row/class
        elif operator == '2':
            """ Modify a spicific data """
            modify(class_data)
            print('\nProcess ends\n')

        # Option 3: Delete a row/class
        elif operator == '3':
            """Delete a row of data with the classname"""
            delete(class_data)

        # Option 4: Show all classes/rows on the console
        elif operator == '4':
            """Show the rows and there index"""
            class_data.showData()

        # Finish the program
        elif operator == '5':
            print('Program End\nThanks for used Clase Manager System')
            del class_data
            break

if __name__ == '__main__':
    main()