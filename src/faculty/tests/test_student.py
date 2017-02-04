"""
test_student Module

Created on 22.11.2016
@author adiM
"""
from unittest import TestCase

from faculty.domain.entities import Student


class TestStudent(TestCase):
    def setUp(self):
        super().setUp()
        self.__student = Student(1, "Mihai")

    def test_student_id(self):
        self.assertEqual(self.__student.student_id, 1, "Student ID should be 1")

    def test_name(self):
        self.assertEqual(self.__student.name, "Mihai", "Student name should be Mihai")
        self.__student.name = "Alin"
        self.assertEqual(self.__student.name, "Alin", "Name must be set to Alin")

    def test_str(self):
        assert (str(self.__student) == "Student ID: 1 || Student Name: Mihai")

    def test_eq(self):
        self.assertEqual(self.__student.__eq__(2), False, "Should be False")

    def test_ne(self):
        self.assertEqual(self.__student.__ne__(2), True, "Should be True")
