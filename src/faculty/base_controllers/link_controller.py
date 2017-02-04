"""
link_controller Module

Created on 20.11.2016
@author adiM
"""

from faculty.domain.entities import Link


class LinkController(object):
    def __init__(self, link_repository):
        self.__link_repository = link_repository
        self.__link_repository.load_enrollment()

    def find_by_id(self, link_id):
        if self.__link_repository.find_link(link_id) is not None:
            return self.__link_repository.find_link(link_id)
        return None

    def add_link(self, discipline_id, student_id):
        link = Link(discipline_id, student_id)
        self.__link_repository.save(link)
        self.__link_repository.save_enrollment()

    def delete_student(self, student_id):
        self.__link_repository.delete_by_student(student_id)
        self.__link_repository.save_enrollment()

    def delete_discipline(self, discipline_id):
        self.__link_repository.delete_by_discipline(discipline_id)
        self.__link_repository.save_enrollment()

    def delete_link(self, link_id):
        self.__link_repository.delete_specific_link(link_id)
        self.__link_repository.save_enrollment()

    def get_all(self):
        return self.__link_repository.get_all()
