# ----------------------------------------------------------------------------------------- #
# Title: Assignment06
# Description: Demonstrates how to use functions in your code
# ChangeLog: (Who, When, What)
#    Jon Bennefeld, 5/21/2024, Copied script from
#      Mod06-Lab03-WorkingWithClassesAndSoC.py and began edits
# ------------------------------------------------------------------------------------------ #

# ------------------------------------------------------------------------------------------ #
# Setup Code:
# Make sure there is some student data in the Enrollments.json file before running
# ------------------------------------------------------------------------------------------ #


import json

# Global Data --------------------------------------- #
FILE_NAME: str = 'Enrollments.json'
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''

menu_choice = ''
students: list = []

# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    Jon Bennefeld, 5/21/2024, Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):

        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
       Jon Bennefeld, 5/21/2024, Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
           Jon Bennefeld, 5/21/2024, Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
           Jon Bennefeld, 5/21/2024, Created function

        :return: None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
           Jon Bennefeld, 5/21/2024, Created function

        :return: string with the user's choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # if the choice is outside the expected choices, give error message
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """ This function displays previously entered student data to the user,
        either from this session or what was in the file when the program began

        ChangeLog: (Who, When, What)
           Jon Bennefeld, 5/21/2024, Created function

        :return: None
        """

        print("\nStudent data =")
        for row in student_data:
            print(f'{row["FirstName"]},{row["LastName"]},{row["CourseName"]}')


    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the first name, last name, and course name from the user

        ChangeLog: (Who, When, What)
           Jon Bennefeld, 5/21/2024, Created function

        :return: None
        """

        try:
            # input the data
            # if the student's first or last name does not contain all letters, raise an error
            student_first_name = input("What is the student's first name? ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should contain letters only.")

            student_last_name = input("What is the student's last name? ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should contain letters only.")

            course_name = input("What is the student's course? ")

            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

# End of function definitions


# Beginning of the main body of this script
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Repeat the follow tasks
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":  # get new data
        students = IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2":  # display current data (including what was read from the file upon start)
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "3":  # save data to the file, and also display what was written to the file
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        print("The following data is written to the file:")
        IO.output_student_courses(student_data=students)
        continue

    elif menu_choice == "4":  # end the program
        break  # out of the while loop
