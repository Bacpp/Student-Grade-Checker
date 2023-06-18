# This is my main file where we create the start() method,
# in, it we initialize instances
# of all the classes from student.py (except Person)
# and then assign them to the School class
# where all the magic of adding them to files
# and sorting them happens. By then running this start method
# in the main section we see what the program does.
# In the case I've currently set it sorts out all students
# with a MAT101 grade above 90.#
#coverage run --source="C:\Users\gevez\Desktop\COS340\PROJECTKirilGevezov" -m unittest discover -s "C:\Users\gevez\Desktop\COS340\PROJECTKirilGevezov"

from student import Student, Course, School
import csv
import configparser



def start(students_file, courses_file):
    """
        Initializes a `School` instance with the given `students_file`
        and `courses_file`. Creates `Student` and `Course` instances,
        adds them to the `School`, and writes them to the respective files.
        Reads `Student` and `Course` data from files using`csv.reader`.
        Selects and prints all students with course code "MATH101" and grade
        greater than 90.

        Args:
            students_file (str): The file path of the CSV file
            containing student data.
            courses_file (str): The file path of the CSV file
             containing course data.

    """
    # Create School instance
    school = School(students_file, courses_file)

    # Create Student and Course instances

    student2 = Student("Georgi", "67890", "ENG101", 92.3)
    student3 = Student("Roman", "22424", "HIT101", 67.5)
    student4 = Student("Apostol", "65756", "HIT101", 96.3)
    student5 = Student("Aleks2", "29482", "MATH101", 92.7)
    student6 = Student("Aleks", "55646", "MATH101", 94.7)
    student1 = Student("Ivan", "12345", "MATH101", 67.2)
    course1 = Course("Math", "MATH101", "Mr. Johnson")
    course2 = Course("English", "ENG101", "Ms. Smith")
    course3 = Course("History", "HIT101", "Mr. Brown")
    course4 = Course("Philosophy", "PHI101", "Ms. Aron")

    # Add students and courses to School instance
    school.add_student(student1)
    school.add_student(student2)
    school.add_student(student3)
    school.add_student(student4)
    school.add_student(student5)
    school.add_student(student6)
    school.add_course(course1)
    school.add_course(course2)
    school.add_course(course3)
    school.add_course(course4)

    # Write students and courses to file
    school.write_students()
    school.write_courses()

    selected_students = school.select_students('MATH101', students_file, 20)
    for student in selected_students:
        print(student.name, student.id_num, student.course, student.grade)


if __name__ == "__main__":
    # create configparser object and read config file
    config = configparser.ConfigParser()
    config.read('config.ini')

    # get file names from config file
    students_file = config['section1']['students']
    courses_file = config['section2']['courses']

    # pass file names to your start function
    start(students_file, courses_file)
