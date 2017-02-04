"""
test_disciplineRepository Module

Created on 28.11.2016
@author adiM
"""
from unittest import TestCase

from faculty.domain.entities import Discipline
from faculty.domain.validators import DisciplineValidator
from faculty.repositories.discipline_repository import DisciplineRepository, DisciplineRepositoryException


class TestDisciplineRepository(TestCase):
    def setUp(self):
        super().setUp()
        self.__discipline_repository = DisciplineRepository(DisciplineValidator)

    def test_save(self):
        d = Discipline(1, "OOP")
        self.__discipline_repository.save(d)
        self.assertEqual(len(self.__discipline_repository.get_all()), 1, "Len should be 1")
        self.assertRaises(DisciplineRepositoryException, self.__discipline_repository.save, d)

    def test_update(self):
        d = Discipline(1, "OOP")
        self.__discipline_repository.save(d)
        d = Discipline(1, "WebDev")
        self.__discipline_repository.update(1, d)
        self.assertEqual(self.__discipline_repository.find_by_id(1), d, "Update not done")
        self.assertRaises(DisciplineRepositoryException, self.__discipline_repository.update, 2, d)

    def test_delete_by_id(self):
        d = Discipline(1, "OOP")
        self.__discipline_repository.save(d)
        d = Discipline(2, "WebDev")
        self.__discipline_repository.save(d)
        self.__discipline_repository.delete_by_id(1)
        self.assertEqual(len(self.__discipline_repository.get_all()), 1, "Len should be 1")
        self.assertRaises(DisciplineRepositoryException, self.__discipline_repository.delete_by_id, 1)
