"""
test_studentRepository Module

Created on 28.11.2016
@author adiM
"""
from unittest import TestCase

from faculty.domain.entities import Student
from faculty.domain.validators import StudentValidator
from faculty.repositories.student_repository import StudentRepository, StudentRepositoryException


class TestStudentRepository(TestCase):
    def setUp(self):
        super().setUp()
        self.__student_repository = StudentRepository(StudentValidator)

    def test_save(self):
        s = Student(1, "Mihai")
        self.__student_repository.save(s)
        self.assertEqual(len(self.__student_repository.get_all()), 1, "There should be 1 element in repo")
        self.assertRaises(StudentRepositoryException, self.__student_repository.save, s)

    def test_update(self):
        s = Student(1, "Mihai")
        self.__student_repository.save(s)
        s = Student(1, "Andrei")
        self.__student_repository.update(1, s)
        self.assertEqual(self.__student_repository.find_by_id(1), s, "Update didn't work")
        s = Student(2, "Alin")
        self.assertRaises(StudentRepositoryException, self.__student_repository.update, 3, s)

    def test_delete_by_id(self):
        s = Student(1, "Mihai")
        self.__student_repository.save(s)
        s = Student(2, "Andrei")
        self.__student_repository.save(s)
        self.__student_repository.delete_by_id(1)
        self.assertEqual(len(self.__student_repository.get_all()), 1, "Only one item left")
        self.assertRaises(StudentRepositoryException, self.__student_repository.delete_by_id, 1)
