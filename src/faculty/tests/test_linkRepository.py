"""
test_linkRepository Module

Created on 02.12.2016
@author adiM
"""
from unittest import TestCase

from faculty.domain.entities import Link
from faculty.domain.validators import LinkValidator
from faculty.repositories.link_repository import LinkRepository, LinkRepositoryException


class TestLinkRepository(TestCase):
    def setUp(self):
        super().setUp()
        self.__link_repository = LinkRepository(LinkValidator)

    def test_save(self):
        l = Link(1, 2)
        self.__link_repository.save(l)
        self.assertEqual(len(self.__link_repository.get_all()), 1, "Len should be one")
        self.assertRaises(LinkRepositoryException, self.__link_repository.save, l)

    def test_delete_by_student(self):
        l = Link(1, 2)
        self.__link_repository.save(l)
        l = Link(1, 1)
        self.__link_repository.save(l)
        l = Link(2, 1)
        self.__link_repository.save(l)
        l = Link(1, 3)
        self.__link_repository.save(l)
        l = Link(5, 1)
        self.__link_repository.save(l)
        self.__link_repository.delete_by_student(1)
        self.assertEqual(len(self.__link_repository.get_all()), 2, "Len Should be 2")

    def test_delete_by_discipline(self):
        l = Link(1, 2)
        self.__link_repository.save(l)
        l = Link(1, 1)
        self.__link_repository.save(l)
        l = Link(2, 1)
        self.__link_repository.save(l)
        l = Link(1, 3)
        self.__link_repository.save(l)
        l = Link(5, 1)
        self.__link_repository.save(l)
        self.__link_repository.delete_by_discipline(1)
        self.assertEqual(len(self.__link_repository.get_all()), 2, "Len should be 2")

    def test_delete_specific_link(self):
        l = Link(1, 2)
        self.__link_repository.save(l)
        l = Link(1, 1)
        self.__link_repository.save(l)
        l = Link(2, 1)
        self.__link_repository.save(l)
        l = Link(1, 3)
        self.__link_repository.save(l)
        l = Link(5, 1)
        self.__link_repository.save(l)
        self.__link_repository.delete_specific_link("2.1")
        self.assertEqual(len(self.__link_repository.get_all()), 4, "Len Should be 4")
