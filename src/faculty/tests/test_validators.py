"""
test_validators Module

Created on 28.11.2016
@author adiM
"""

from unittest import TestCase

from faculty.domain.entities import Student, Discipline, Grade, Link
from faculty.domain.validators import StudentValidator, StudentValidatorException, DisciplineValidator, \
    DisciplineValidatorException, GradeValidator, GradeValidatorException, LinkValidator, LinkValidatorException


class TestStudentValidator(TestCase):
    def setUp(self):
        super().setUp()
        self.__stud_validator = StudentValidator
        self.__dis_validator = DisciplineValidator
        self.__grade_validator = GradeValidator
        self.__link_validator = LinkValidator

    def test_student_validator(self):
        s = Student("s", "Mihai")
        self.assertRaises(StudentValidatorException, self.__stud_validator.validate, s)
        s = Student(-2, "Mihai")
        self.assertRaises(StudentValidatorException, self.__stud_validator.validate, s)
        s = Student(1, 15)
        self.assertRaises(StudentValidatorException, self.__stud_validator.validate, s)

    def test_discipline_validator(self):
        d = Discipline("d", "OOP")
        self.assertRaises(DisciplineValidatorException, self.__dis_validator.validate, d)
        d = Discipline(-1, "OOP")
        self.assertRaises(DisciplineValidatorException, self.__dis_validator.validate, d)
        d = Discipline(1, 3)
        self.assertRaises(DisciplineValidatorException, self.__dis_validator.validate, d)

    def test_grade_validator(self):
        g = Grade(-1, 1, 10)
        self.assertRaises(GradeValidatorException, self.__grade_validator.validate, g)
        g = Grade(1, "s", 10)
        self.assertRaises(GradeValidatorException, self.__grade_validator.validate, g)
        g = Grade(1, 1, 15)
        self.assertRaises(GradeValidatorException, self.__grade_validator.validate, g)

    def test_link_validator(self):
        l = Link("s", 2)
        self.assertRaises(LinkValidatorException, self.__link_validator.validate, l)
        l = Link(1, -2)
        self.assertRaises(LinkValidatorException, self.__link_validator.validate, l)
