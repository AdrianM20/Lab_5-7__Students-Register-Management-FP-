"""
student_controller Module

Created on 06.11.2016
@author adiM
"""

from faculty.domain.entities import Student


class StudentController(object):
    def __init__(self, student_repository):
        self.__student_repository = student_repository
        self.__student_repository.load_students()

    def find_by_id(self, student_id):
        if self.__student_repository.find_by_id(student_id) is not None:
            return self.__student_repository.find_by_id(student_id)
        return None

    def add_student(self, student_id, name):
        student = Student(student_id, name)
        self.__student_repository.save(student)
        self.__student_repository.save_students()

    def remove_student(self, student_id):
        self.__student_repository.delete_by_id(student_id)
        self.__student_repository.save_students()

    def update_student(self, student_id, name):
        student = Student(student_id, name)
        self.__student_repository.update(student_id, student)
        self.__student_repository.save_students()

    def get_all(self):
        return self.__student_repository.get_all()
