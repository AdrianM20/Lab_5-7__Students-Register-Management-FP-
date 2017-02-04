"""
test_discipline Module

Created on 26.11.2016
@author adiM
"""
from unittest import TestCase

from faculty.domain.entities import Discipline


class TestDiscipline(TestCase):
    def setUp(self):
        super().setUp()
        self.__discipline = Discipline(1, "OOP")

    def test_discipline_id(self):
        self.assertEqual(self.__discipline.discipline_id, 1, "Discipline ID should be 1")

    def test_name(self):
        self.assertEqual(self.__discipline.name, "OOP", "Discipline name should be OOP")
        self.__discipline.name = "WebDev"
        self.assertEqual(self.__discipline.name, "WebDev", "Name should be set to WebDev")

    def test_str(self):
        assert (str(self.__discipline) == "Discipline ID: 1 || Discipline Name: OOP")

    def test_eq(self):
        self.assertEqual(self.__discipline.__eq__(4), False, "Should be False")

    def test_ne(self):
        self.assertEqual(self.__discipline.__ne__(4), True, "Should be True")
