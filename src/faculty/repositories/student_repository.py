"""
entity_repository Module

Created on 04.11.2016
@author adiM
"""

from faculty.domain.validators import FacultyException


class StudentRepositoryException(FacultyException):
    pass


class StudentRepository(object):
    """
    Class that stores and performs operations on student objects
    """

    def __init__(self, validator_class):
        self.__validator_class = validator_class
        self._students = {}
        # self.__filename = filename

    def find_by_id(self, student_id):
        """
        Returns the student identified by student_id
        args:
            student_id - the id by which to search
        returns:
            student stored with id = student_id
            None if not found
        """
        if student_id in self._students:
            return self._students[student_id]
        return None

    def init_save(self, student):
        if self.find_by_id(student.student_id) is not None:
            raise StudentRepositoryException(
                "Duplicate error. Student ID {0} already registered.".format(student.student_id))
        self.__validator_class.validate(student)
        self._students[student.student_id] = student

    def save(self, student):
        """
        Adds student object to the dictionary at key = student.student_id
        args:
            student - object to be added to repositories
        exception:
                StudentRepositoryException if student.student.student_id is already taken
        """
        if self.find_by_id(student.student_id) is not None:
            raise StudentRepositoryException(
                "Duplicate error. Student ID {0} already registered.".format(student.student_id))
        self.__validator_class.validate(student)
        self._students[student.student_id] = student
        # self.__save_to_file()

    def update(self, student_id, student):
        if self.find_by_id(student_id) is None:
            raise StudentRepositoryException(
                "Student data cannot be updated because student ID {0} is not registered yet.".format(student_id))
        self.__validator_class.validate(student)
        self._students[student_id] = student
        # self.__save_to_file()

    def delete_by_id(self, student_id):
        if self.find_by_id(student_id) is None:
            raise StudentRepositoryException("Student ID {0} does not exist. No data deleted".format(student_id))
        del self._students[student_id]
        # self.__save_to_file()

    def get_all(self):
        return self._students.values()

    def load_students(self):
        pass

    def save_students(self):
        pass


'''
    def __save_to_file(self):
        f = open(self.__filename, "w")
        try:
            for s in self.get_all():
                sString = str(s.student_id) + ", " + s.name + "\n"
                f.write(sString)
            f.close()
        except Exception as e:
            print("An error occurred in file saving:")
            print(str(e))
'''
