"""
pickle_repository Module

Created on 09.01.2017
@author adiM
"""

import pickle
from faculty.domain.validators import FacultyException
from faculty.repositories.student_repository import StudentRepository
from faculty.repositories.discipline_repository import DisciplineRepository
from faculty.repositories.grade_repository import GradeRepository
from faculty.repositories.link_repository import LinkRepository


class PickleRepositoryException(FacultyException):
    pass


class StudentPickleRepository(StudentRepository):
    def __init__(self, ValidatorClass, filename):
        super().__init__(ValidatorClass)
        self.__ValidatorClass = ValidatorClass
        self.__filename = filename

    def load_students(self):
        try:
            with open(self.__filename, "rb") as f:
                data = pickle.load(f)
                self._students = data
            f.close()
        except EOFError:
            self._students = {}
        except IOError:
            raise PickleRepositoryException("File: {0} is missing".format(self.__filename))

    def save_students(self):
        f = open(self.__filename, "wb")
        data = self._students
        pickle.dump(data, f)
        f.close()


class DisciplinePickleRepository(DisciplineRepository):
    def __init__(self, ValidatorClass, filename):
        super().__init__(ValidatorClass)
        self.__ValidatorClass = ValidatorClass
        self.__filename = filename

    def load_disciplines(self):
        try:
            with open(self.__filename, "rb") as f:
                data = pickle.load(f)
                self._disciplines = data
            f.close()
        except EOFError:
            self._disciplines = {}
        except IOError:
            raise PickleRepositoryException("File: {0} is missing".format(self.__filename))

    def save_disciplines(self):
        f = open(self.__filename, "wb")
        data = self._disciplines
        pickle.dump(data, f)
        f.close()


class LinkPickleRepository(LinkRepository):
    def __init__(self, ValidatorClass, filename):
        super().__init__(ValidatorClass)
        self.__ValidatorClass = ValidatorClass
        self.__filename = filename

    def load_enrollment(self):
        try:
            with open(self.__filename, "rb") as f:
                data = pickle.load(f)
                self._links = data
            f.close()
        except EOFError:
            self._links = {}
        except IOError:
            raise PickleRepositoryException("File: {0} is missing".format(self.__filename))

    def save_enrollment(self):
        f = open(self.__filename, "wb")
        data = self._links
        pickle.dump(data, f)
        f.close()


class GradePickleRepository(GradeRepository):
    def __init__(self, ValidatorClass, filename):
        super().__init__(ValidatorClass)
        self.__ValidatorClass = ValidatorClass
        self.__filename = filename

    def load_grades(self):
        try:
            with open(self.__filename, "rb") as f:
                data = pickle.load(f)
                self._grades = data
            f.close()
        except EOFError:
            self._grades = []
        except IOError:
            raise PickleRepositoryException("File: {0} is missing".format(self.__filename))

    def save_grades(self):
        f = open(self.__filename, "wb")
        data = self._grades
        pickle.dump(data, f)
        f.close()
