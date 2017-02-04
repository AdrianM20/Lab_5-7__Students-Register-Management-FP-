"""
test_link Module

Created on 26.11.2016
@author adiM
"""
from unittest import TestCase

from faculty.domain.entities import Link


class TestLink(TestCase):
    def setUp(self):
        super().setUp()
        self.__link = Link(1, 2)

    def test_link_id(self):
        self.assertEqual(self.__link.link_id, "1.2", "Link should be 1.2")

    def test_discipline_id(self):
        self.assertEqual(self.__link.discipline_id, 1, "Discipline ID should be 1")

    def test_student_id(self):
        self.assertEqual(self.__link.student_id, 2, "Student ID should be 2")

    def test_str(self):
        assert (str(self.__link) == "Student with ID 2 is enrolled at discipline with ID 1")
