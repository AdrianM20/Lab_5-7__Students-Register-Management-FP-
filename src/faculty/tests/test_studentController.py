"""
test_studentController Module

Created on 02.12.2016
@author adiM
"""
from unittest import TestCase

from faculty.base_controllers.student_controller import StudentController
from faculty.domain.entities import Student
from faculty.domain.validators import StudentValidator
from faculty.repositories.student_repository import StudentRepository


class TestStudentController(TestCase):
    def setUp(self):
        super().setUp()
        self.__student_repository = StudentRepository(StudentValidator)
        self.__student_controller = StudentController(self.__student_repository)

    def test_find_by_id(self):
        self.__student_controller.add_student(1, "Alin")
        self.__student_controller.add_student(2, "Mircea")
        self.assertEqual(self.__student_controller.find_by_id(2), self.__student_repository.find_by_id(2),
                         "Student Mircea should be returned")
        self.assertEqual(self.__student_controller.find_by_id(3), None, "None should be returned")

    def test_add_student(self):
        self.__student_controller.add_student(1, "Alin")
        self.__student_controller.add_student(2, "Mircea")
        self.assertEqual(len(self.__student_controller.get_all()), 2, "Len should be 2")

    def test_remove_student(self):
        self.__student_controller.add_student(1, "Alin")
        self.__student_controller.add_student(2, "Mircea")
        self.__student_controller.add_student(3, "Mihai")
        self.__student_controller.remove_student(2)
        self.assertEqual(len(self.__student_controller.get_all()), 2, "Len should be 2")

    def test_update_student(self):
        self.__student_controller.add_student(1, "Alin")
        self.__student_controller.add_student(2, "Mircea")
        self.__student_controller.add_student(3, "Mihai")
        self.__student_controller.update_student(2, "Andrei")
        s = self.__student_controller.find_by_id(2)
        self.assertEqual(s.name, "Andrei", "Name should be Andrei")
