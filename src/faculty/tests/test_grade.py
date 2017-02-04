"""
test_grade Module

Created on 26.11.2016
@author adiM
"""
from unittest import TestCase

from faculty.domain.entities import Grade


class TestGrade(TestCase):
    def setUp(self):
        super().setUp()
        self.__grade = Grade(1, 2, 10)

    def test_discipline_id(self):
        self.assertEqual(self.__grade.discipline_id, 1, "Discipline ID should be 1")
        self.__grade.discipline_id = 3
        self.assertEqual(self.__grade.discipline_id, 3, "Discipline ID should be set to 3")

    def test_student_id(self):
        self.assertEqual(self.__grade.student_id, 2, "Student ID should be 2")
        self.__grade.student_id = 1
        self.assertEqual(self.__grade.student_id, 1, "Student ID should be set to 1")

    def test_grade_value(self):
        self.assertEqual(self.__grade.grade_value, 10, "Grade should be 10")
        self.__grade.grade_value = 6
        self.assertEqual(self.__grade.grade_value, 6, "Grade should be set to 6")

    def test_str(self):
        assert (str(self.__grade) == "Discipline ID: 1 || Student ID: 2 || Grade: 10")
