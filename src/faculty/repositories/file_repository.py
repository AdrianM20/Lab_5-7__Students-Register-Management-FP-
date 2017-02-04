"""
file_repository Module

Created on 11.12.2016
@author adiM
"""

from faculty.domain.entities import Student, Discipline, Grade, Link
from faculty.domain.validators import FacultyException
from faculty.repositories.student_repository import StudentRepository
from faculty.repositories.discipline_repository import DisciplineRepository
from faculty.repositories.grade_repository import GradeRepository
from faculty.repositories.link_repository import LinkRepository


class FileRepositoryException(FacultyException):
    pass


class StudentFileRepository(StudentRepository):
    def __init__(self, ValidatorClass, filename):
        super().__init__(ValidatorClass)
        self.__ValidatorClass = ValidatorClass
        self.__filename = filename
        # self.__load_students()

    def load_students(self):
        try:
            with open(self.__filename) as f:
                for line in f:
                    args = line.split(',')
                    student_id = int(args[0].strip())
                    name = args[1].strip()
                    student = Student(student_id, name)
                    self.init_save(student)
                f.close()
        except IOError:
            raise FileRepositoryException("File: {0} is missing".format(self.__filename))

    def save_students(self):
        f = open(self.__filename, "w")
        try:
            for s in self.get_all():
                sString = str(s.student_id) + ", " + s.name + "\n"
                f.write(sString)
            f.close()
        except Exception as e:
            print("An error occurred in file saving:")
            print(str(e))


class DisciplineFileRepository(DisciplineRepository):
    def __init__(self, ValidatorClass, filename):
        super().__init__(ValidatorClass)
        self.__ValidatorClass = ValidatorClass
        self.__filename = filename
        # self.__load_disciplines()

    def load_disciplines(self):
        try:
            with open(self.__filename) as f:
                for line in f:
                    args = line.split(',')
                    discipline_id = int(args[0].strip())
                    name = args[1].strip()
                    discipline = Discipline(discipline_id, name)
                    self.init_save(discipline)
                f.close()
        except IOError:
            raise FileRepositoryException("File: {0} is missing".format(self.__filename))

    def save_disciplines(self):
        f = open(self.__filename, "w")
        try:
            for d in self.get_all():
                dString = str(d.discipline_id) + ", " + d.name + "\n"
                f.write(dString)
            f.close()
        except Exception as e:
            print("An error occurred in file saving: ")
            print(str(e))


class LinkFileRepository(LinkRepository):
    def __init__(self, ValidatorClass, filename):
        super().__init__(ValidatorClass)
        self.__ValidatorClass = ValidatorClass
        self.__filename = filename
        # self.__load_enrollment()

    def load_enrollment(self):
        try:
            with open(self.__filename) as f:
                for line in f:
                    args = line.split(',')
                    discipline_id = int(args[0].strip())
                    student_id = int(args[1].strip())
                    link = Link(discipline_id, student_id)
                    self.init_save(link)
                f.close()
        except IOError:
            raise FileRepositoryException("File: {0} is missing".format(self.__filename))

    def save_enrollment(self):
        f = open(self.__filename, "w")
        try:
            for l in self.get_all():
                lString = str(l.discipline_id) + ", " + str(l.student_id) + "\n"
                f.write(lString)
            f.close()
        except Exception as e:
            print("An error occurred in file saving:")
            print(str(e))


class GradeFileRepository(GradeRepository):
    def __init__(self, ValidatorClass, filename):
        super().__init__(ValidatorClass)
        self.__ValidatorClass = ValidatorClass
        self.__filename = filename
        # self.__load_grades()

    def load_grades(self):
        try:
            with open(self.__filename) as f:
                for line in f:
                    args = line.split(',')
                    discipline_id = int(args[0].strip())
                    student_id = int(args[1].strip())
                    grade_value = int(args[2].strip())
                    grade = Grade(discipline_id, student_id, grade_value)
                    self.init_save(grade)
                f.close()
        except IOError:
            raise FileRepositoryException("File: {0} is missing".format(self.__filename))

    def save_grades(self):
        f = open(self.__filename, "w")
        try:
            for g in self.get_all():
                gString = str(g.discipline_id) + ", " + str(g.student_id) + ", " + str(g.grade_value) + "\n"
                f.write(gString)
            f.close()
        except Exception as e:
            print("An error occurred in file saving:")
            print(str(e))
