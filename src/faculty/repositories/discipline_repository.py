"""
discipline_repository Module

Created on 08.11.2016
@author adiM
"""

from faculty.domain.validators import FacultyException


class DisciplineRepositoryException(FacultyException):
    pass


class DisciplineRepository(object):
    def __init__(self, validator_class):
        self.__validator_class = validator_class
        self._disciplines = {}
        # self.__filename = filename

    def find_by_id(self, discipline_id):
        if discipline_id in self._disciplines:
            return self._disciplines[discipline_id]
        return None

    def init_save(self, discipline):
        if self.find_by_id(discipline.discipline_id) is not None:
            raise DisciplineRepositoryException(
                "Discipline ID {0} already registered.".format(discipline.discipline_id))
        self.__validator_class.validate(discipline)
        self._disciplines[discipline.discipline_id] = discipline

    def save(self, discipline):
        if self.find_by_id(discipline.discipline_id) is not None:
            raise DisciplineRepositoryException(
                "Discipline ID {0} already registered.".format(discipline.discipline_id))
        self.__validator_class.validate(discipline)
        self._disciplines[discipline.discipline_id] = discipline
        # self.__save_to_file()

    def update(self, discipline_id, discipline):
        if self.find_by_id(discipline_id) is None:
            raise DisciplineRepositoryException(
                "Discipline data cannot be updated because discipline ID {0} is not registered yet.".format(
                    discipline_id))
        self.__validator_class.validate(discipline)
        self._disciplines[discipline_id] = discipline
        # self.__save_to_file()

    def delete_by_id(self, discipline_id):
        if self.find_by_id(discipline_id) is None:
            raise DisciplineRepositoryException(
                "Discipline ID {0} does not exist. No data deleted".format(discipline_id))
        del self._disciplines[discipline_id]
        # self.__save_to_file()

    def get_all(self):
        return self._disciplines.values()

    def load_disciplines(self):
        pass

    def save_disciplines(self):
        pass


'''
    def __save_to_file(self):
        f = open(self.__filename, "w")
        try:
            for d in self.get_all():
                dString = str(d.discipline_id) + ", " + d.name + "\n"
                f.write(dString)
            f.close()
        except Exception as e:
            print("An error occurred in file saving:")
            print(str(e))
'''
