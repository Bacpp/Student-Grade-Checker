# In here we create unit tests for some methods
# in the student.py file in order to check whether they work properly#

import os
import csv
import unittest
from student import Student, Course, School


class TestStudent(unittest.TestCase):
    def test_init(self):
        """Test the initialization of a Student instance."""
        student = Student("Alice", "12345", "MATH101", 87.5)
        self.assertEqual(student.name, "Alice")
        self.assertEqual(student.id_num, "12345")
        self.assertEqual(student.course, "MATH101")
        self.assertEqual(student.grade, 87.5)

    def setUp(self):
        """Set up a Student instance for testing."""
        self.student = Student("Kir", "23424", "MATH101", 87.2)

    def test_get_id_num(self):
        """Test the get_id_num method of a Student instance."""
        self.student.set_id_num("12345")
        self.assertEqual(self.student.get_id_num(), "12345")

    def test_set_id_num(self):
        """Test the set_id_num method of a Student instance."""
        self.student.set_id_num("54321")
        self.assertEqual(self.student.get_id_num(), "54321")

    def test_get_course(self):
        """Test the get_course method of a Student instance."""
        self.student.set_course("Math")
        self.assertEqual(self.student.get_course(), "Math")

    def test_set_course(self):
        """Test the set_course method of a Student instance."""
        self.student.set_course("English")
        self.assertEqual(self.student.get_course(), "English")

    def test_get_grade(self):
        """Test the get_grade method of a Student instance."""
        self.student.set_grade(85)
        self.assertEqual(self.student.get_grade(), 85)

    def test_set_grade(self):
        """Test the set_grade method of a Student instance."""
        self.student.set_grade(90)
        self.assertEqual(self.student.get_grade(), 90)

    def test_str(self):
        """Test whether the __str__ method prints out everything properly."""
        student = Student("Alice", "12345", "ENG101", 87.5)
        self.assertEqual(str(student), "Alice (ID: 12345) - "
                                       "Course: ENG101 - Grade: 87.5")


class TestCourse(unittest.TestCase):
    def test_init(self):
        """Test the initialization of a Course instance."""
        course = Course("Math", "MATH101", "Mr. Johnson")
        self.assertEqual(course.name, "Math")
        self.assertEqual(course.code, "MATH101")
        self.assertEqual(course.teacher, "Mr. Johnson")

    def test_str(self):
        """Test whether the __str__ method prints out everything properly."""
        course = Course("Math", "MATH101", "Mr. Johnson")
        self.assertEqual(str(course), "Math (MATH101) - Teacher: Mr. Johnson")


class TestSchool(unittest.TestCase):
    def setUp(self):
        """Set up a School instance for testing."""
        self.school = School("students_file.txt", "courses.txt")

    def test_add_student(self):
        """Testing whether when I use the add_student method it actually adds it to the list."""
        student = Student("Alice", "12345", "MATH101", 87.5)
        self.school.add_student(student)
        self.assertIn(student, self.school.students)

    def test_add_course(self):
        """Testing whether when I use the add_course method it actually adds it to the list."""
        course = Course("Math", "MATH101", "Mr. Johnson")
        self.school.add_course(course)
        self.assertIn(course, self.school.courses)

    def test_write_students(self):
        """Testing whether when I use the write_students method it gets added to the file."""
        # Create a new School instance with some students
        school = School("test_students.csv", "test_courses.csv")
        alice = Student("Alice", "1234", "Math", 80.3)
        school.add_student(alice)

        # Write the students to a test CSV file
        school.write_students()

        # Read the test file and check that the data was written correctly
        with open("test_students.csv", "r") as f:
            reader = csv.reader(f)
            rows = [row for row in reader]
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0], ["Alice", "1234", "Math", "80.3"])

    def test_write_courses(self):
        """Testing whether when I use the write_courses method it gets added to the file."""
        # Create a new School instance with some students
        school = School("test_students.csv", "test_courses.csv")
        python = Course("COS340", "Python", "Prof. Mitreva")
        school.add_course(python)

        # Write the students to a test CSV file
        school.write_courses()

        # Read the test file and check that the data was written correctl
        with open("test_courses.csv", "r") as f:
            reader = csv.reader(f)
            rows = [row for row in reader]
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0], ["COS340", "Python", "Prof. Mitreva"])

if __name__ == "__main__":
    unittest.main()
