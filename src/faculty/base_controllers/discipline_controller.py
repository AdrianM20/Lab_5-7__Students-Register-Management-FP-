"""
discipline_controller Module

Created on 07.11.2016
@author adiM
"""

from faculty.domain.entities import Discipline


class DisciplineController(object):
    def __init__(self, discipline_repository):
        self.__discipline_repository = discipline_repository
        self.__discipline_repository.load_disciplines()

    def find_by_id(self, discipline_id):
        if self.__discipline_repository.find_by_id(discipline_id) is not None:
            return self.__discipline_repository.find_by_id(discipline_id)
        return None

    def add_discipline(self, discipline_id, name):
        discipline = Discipline(discipline_id, name)
        self.__discipline_repository.save(discipline)
        self.__discipline_repository.save_disciplines()

    def remove_discipline(self, discipline_id):
        self.__discipline_repository.delete_by_id(discipline_id)
        self.__discipline_repository.save_disciplines()

    def update_discipline(self, discipline_id, name):
        discipline = Discipline(discipline_id, name)
        self.__discipline_repository.update(discipline_id, discipline)
        self.__discipline_repository.save_disciplines()

    def get_all(self):
        return self.__discipline_repository.get_all()
