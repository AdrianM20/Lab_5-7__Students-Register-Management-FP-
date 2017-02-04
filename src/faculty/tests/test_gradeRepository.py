"""
test_gradeRepository Module

Created on 28.11.2016
@author adiM
"""
from unittest import TestCase

from faculty.domain.entities import Grade
from faculty.domain.validators import GradeValidator
from faculty.repositories.grade_repository import GradeRepository, GradeRepositoryException


class TestGradeRepository(TestCase):
    def setUp(self):
        super().setUp()
        self.__grade_repository = GradeRepository(GradeValidator)

    def test_save(self):
        g = Grade(1, 2, 10)
        self.__grade_repository.save(g)
        self.assertEqual(len(self.__grade_repository.get_all()), 1, "len should be 1")

    def test_delete_by_student(self):
        g = Grade(1, 2, 10)
        self.__grade_repository.save(g)
        g = Grade(1, 1, 8)
        self.__grade_repository.save(g)
        g = Grade(2, 1, 5)
        self.__grade_repository.save(g)
        g = Grade(1, 3, 7)
        self.__grade_repository.save(g)
        g = Grade(5, 1, 8)
        self.__grade_repository.save(g)
        self.__grade_repository.delete_by_student(1)
        self.assertEqual(len(self.__grade_repository.get_all()), 2, "Len should be 2")
        # self.assertRaises(GradeRepositoryException, self.__grade_repository.delete_by_student, 4)

    def test_delete_by_discipline(self):
        g = Grade(1, 2, 10)
        self.__grade_repository.save(g)
        g = Grade(1, 1, 8)
        self.__grade_repository.save(g)
        g = Grade(2, 1, 5)
        self.__grade_repository.save(g)
        g = Grade(1, 3, 7)
        self.__grade_repository.save(g)
        g = Grade(5, 1, 8)
        self.__grade_repository.save(g)
        self.__grade_repository.delete_by_discipline(1)
        self.assertEqual(len(self.__grade_repository.get_all()), 2, "Len should be 2")
        # self.assertRaises(GradeRepositoryException, self.__grade_repository.delete_by_discipline, 3)

    def test_delete_specific_grade(self):
        g = Grade(1, 2, 10)
        self.__grade_repository.save(g)
        g = Grade(1, 1, 8)
        self.__grade_repository.save(g)
        g = Grade(2, 1, 5)
        self.__grade_repository.save(g)
        g = Grade(1, 3, 7)
        self.__grade_repository.save(g)
        g = Grade(5, 1, 8)
        self.__grade_repository.save(g)
        g = Grade(1, 3, 7)
        self.__grade_repository.delete_specific_grade(g)
        self.assertEqual(len(self.__grade_repository.get_all()), 4, "Len Should be 4")
