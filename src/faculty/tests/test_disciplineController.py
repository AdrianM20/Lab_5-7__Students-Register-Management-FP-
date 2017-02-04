"""
test_disciplineController Module

Created on 02.12.2016
@author adiM
"""
from unittest import TestCase

from faculty.base_controllers.discipline_controller import DisciplineController
from faculty.domain.validators import DisciplineValidator
from faculty.repositories.discipline_repository import DisciplineRepository


class TestDisciplineController(TestCase):
    def setUp(self):
        super().setUp()
        self.__discipline_repository = DisciplineRepository(DisciplineValidator)
        self.__discipline_controller = DisciplineController(self.__discipline_repository)

    def test_add_discipline(self):
        self.__discipline_controller.add_discipline(1, "OOP")
        if self.__discipline_controller.find_by_id(2) is None:
            if self.__discipline_controller.find_by_id(1) == self.__discipline_repository.find_by_id(1):
                self.__discipline_controller.add_discipline(2, "WebDev")
        self.assertEqual(len(self.__discipline_controller.get_all()), 2, "Len should be 2")

    def test_remove_discipline(self):
        self.__discipline_controller.add_discipline(1, "OOP")
        self.__discipline_controller.add_discipline(2, "WebDev")
        self.__discipline_controller.add_discipline(3, "Java")
        self.__discipline_controller.remove_discipline(3)
        self.assertEqual(len(self.__discipline_controller.get_all()), 2, "Len should be 2")

    def test_update_discipline(self):
        self.__discipline_controller.add_discipline(1, "OOP")
        self.__discipline_controller.add_discipline(2, "WebDev")
        self.__discipline_controller.add_discipline(3, "Java")
        self.__discipline_controller.update_discipline(2, "C++")
        s = self.__discipline_controller.find_by_id(2)
        self.assertEqual(s.name, "C++", "Name should be C++")
