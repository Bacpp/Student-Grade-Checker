# In this file I've created the person, student, school
# and course classes. These are the essential classes for my project
# as it is a Student Management System (sort of)
# The student class inherits person and is used to create
# instances of students, which can be later
# assigned to the school class. Same goes for the course class.#

import csv


class Person:
    def __init__(self, name):
        """
            Initializes a new instance of the Person class.

            Args:
                name (str): The name of the person.
        """
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, id_num, course, grade):
        """
            Initializes a new instance of the Student class.

            Args:
                name (str): The name of the student.
                id_num (str): The ID of the student.
                course(str): The name of the course the student is taking
                grade (float): The grade of the student.
        """
        super().__init__(name)
        self.id_num = id_num
        self.grade = grade
        self.course = course

    def get_id_num(self):
        return self.id_num

    def set_id_num(self, id_num):
        self.id_num = id_num

    def get_course(self):
        return self.course

    def set_course(self, course):
        self.course = course

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade

    def __str__(self):
        """
            Returns a string representation of the student.
        """
        return f"{self.name} (ID: {self.id_num}) - " \
               f"Course: {self.course} - Grade: {self.grade}"


class Course:
    def __init__(self, name, code, teacher):
        """
            Initializes a new instance of the Course class.

            Args:
                name (str): The name of the course.
                code (str): The code of the course.
                teacher (str): The name of the teacher.
        """
        self.name = name
        self.code = code
        self.teacher = teacher

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_code(self):
        return self.code

    def set_code(self, code):
        self.code = code

    def get_teacher(self):
        return self.teacher

    def set_teacher(self, teacher):
        self.teacher = teacher

    def __str__(self):
        """
            Returns a string representation of the course.
        """
        return f"{self.name} ({self.code}) - Teacher: {self.teacher}"


class School:
    def __init__(self, students_file, courses_file):
        """
            Initializes a new instance of the School class.

            Args:
                students_file (str): The name of the file containing
                 the student's data.
                courses_file (str): The name of the file containing
                 the course's data.
        """
        self.students_file = students_file
        self.courses_file = courses_file
        self.students = []
        self.courses = []

    def add_student(self, student):
        """
            Adds a student to the list of students.

            Args:
                student (Student): The student to add.
        """
        self.students.append(student)

    def add_course(self, course):
        """
            Adds a course to the list of courses.

            Args:
                course (Course): The course to add.
        """
        self.courses.append(course)

    def write_students(self):
        """
            Writes the students data into the file
            and populates the students list.
        """
        with open(self.students_file, "w") as f:
            writer = csv.writer(f)
            for student in self.students:
                writer.writerow([student.get_name(),
                                 student.get_id_num(), student.get_course(),
                                 student.get_grade()])

    def write_courses(self):
        """
            Writes the courses data into the file and populates
            the courses list.
        """
        with open(self.courses_file, "w") as f:
            writer = csv.writer(f)
            for course in self.courses:
                writer.writerow([course.get_name(),
                                 course.get_code(), course.get_teacher()])

    def select_students(self, course_code, students_file, mingrade):
        """
        Args:
            course_code (str): The course code to filter by.

        Returns:
            A list of Student objects that are taking the
             specified course and have a grade greater than mingrade.
        """
        students = []
        with open(students_file) as students_file:
            csv_reader = csv.reader(students_file)
            for row in csv_reader:
                if row:
                    name, id_num, course, grade = row
                    if course == course_code and float(grade) > mingrade:
                        students.append(Student(name, id_num,
                                                course, float(grade)))
        return students
