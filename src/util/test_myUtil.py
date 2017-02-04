"""
test_myUtil Module

Created on 02.12.2016
@author adiM
"""
from unittest import TestCase
from util.common import MyUtil


class TestMyUtil(TestCase):
    def setUp(self):
        super().setUp()
        self.__match = MyUtil.match

    def test_match(self):
        t = "Masina"
        s = "aSi"
        self.assertEqual(self.__match(s, t), True)
