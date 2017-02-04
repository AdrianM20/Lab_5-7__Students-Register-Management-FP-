"""
grade_controller Module

Created on 07.11.2016
@author adiM
"""

from faculty.domain.entities import Grade


class GradeController(object):
    def __init__(self, grade_repository):
        self.__grade_repository = grade_repository
        self.__grade_repository.load_grades()

    def add_grade(self, discipline_id, student_id, grade_value):
        grade = Grade(discipline_id, student_id, grade_value)
        self.__grade_repository.save(grade)
        self.__grade_repository.save_grades()

    def delete_discipline(self, discipline_id):
        self.__grade_repository.delete_by_discipline(discipline_id)
        self.__grade_repository.save_grades()

    def delete_student(self, student_id):
        self.__grade_repository.delete_by_student(student_id)
        self.__grade_repository.save_grades()

    def delete_grade(self, discipline_id, student_id, grade_value):
        grade = Grade(discipline_id, student_id, grade_value)
        self.__grade_repository.delete_specific_grade(grade)
        self.__grade_repository.save_grades()

    def get_all(self):
        return self.__grade_repository.get_all()
