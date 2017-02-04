"""
validators Module

Created on 02.11.2016
@author adiM
"""


class FacultyException(Exception):
    pass


class StudentValidatorException(FacultyException):
    pass


class DisciplineValidatorException(FacultyException):
    pass


class GradeValidatorException(FacultyException):
    pass


class LinkValidatorException(FacultyException):
    pass


class StudentValidator(object):
    @staticmethod
    def validate(student):
        if type(student.student_id) is not int or student.student_id < 0:
            raise StudentValidatorException("Student ID must be an integer greater than 0.")
        if type(student.name) is not str:
            raise StudentValidatorException("Invalid name type for student name.")


class DisciplineValidator(object):
    @staticmethod
    def validate(discipline):
        if type(discipline.discipline_id) is not int or discipline.discipline_id < 0:
            raise DisciplineValidatorException("Discipline ID must be an integer greater than 0.")
        if type(discipline.name) is not str:
            raise DisciplineValidatorException("Invalid name type discipline name")


class GradeValidator(object):
    @staticmethod
    def validate(grade):
        if type(grade.discipline_id) is not int or grade.discipline_id < 0:
            raise GradeValidatorException("Discipline ID must be an integer greater than 0.")
        if type(grade.student_id) is not int or grade.student_id < 0:
            raise GradeValidatorException("Student ID must be an integer greater than 0.")
        if type(grade.grade_value) is not int or grade.grade_value < 1 or grade.grade_value > 10:
            raise GradeValidatorException("Grade value must be an integer from 1 to 10.")


class LinkValidator(object):
    @staticmethod
    def validate(link):
        if type(link.discipline_id) is not int or link.discipline_id < 0:
            raise LinkValidatorException("Discipline ID must be an integer greater than 0")
        if type(link.student_id) is not int or link.student_id < 0:
            raise LinkValidatorException("Student ID must be an integer greater than 0")
