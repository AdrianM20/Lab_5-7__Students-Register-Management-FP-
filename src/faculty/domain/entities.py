"""
entities Module

Created on 02.11.2016
@author adiM
"""


class Student(object):
    """
    Class that defines student entities
    constructor:
        Student(student_id, name)
    properties:
        student_id
        name
    setters:
        name
    """
    def __init__(self, student_id, name):
        self.__student_id = student_id
        self.__name = name

    @property
    def student_id(self):
        return self.__student_id

    # @student_id.setter
    # def student_id(self, value):
    #     self.__student_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return str("Student ID: {0} || Student Name: {1}".format(self.__student_id, self.__name))

    def __eq__(self, other):
        if other is None or type(other) != Student:
            return False
        return self.student_id == other.student_id

    def __ne__(self, other):
        return not self.__eq__(other)


class Discipline(object):
    """
        Class that defines discipline entities
        constructor:
            Discipline(discipline_id, name)
        properties:
            discipline_id
            name
        setters:
            name
        """
    def __init__(self, discipline_id, name):
        self.__discipline_id = discipline_id
        self.__name = name

    @property
    def discipline_id(self):
        return self.__discipline_id

    # @discipline_id.setter
    # def discipline_id(self, value):
    #     self.__discipline_id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return str("Discipline ID: {0} || Discipline Name: {1}".format(self.__discipline_id, self.__name))

    def __eq__(self, other):
        if other is None or type(other) != Discipline:
            return False
        return self.discipline_id == other.discipline_id

    def __ne__(self, other):
        return not self.__eq__(other)


class Grade(object):
    """
        Class that defines grade entities
        constructor:
            Grade(discipline_id, student_id, grade_value)
        properties:
            discipline_id
            student_id
            grade_value
        setters:
            discipline_id
            student_id
            grade_value
        """
    def __init__(self, discipline_id, student_id, grade_value):
        self.__discipline_id = discipline_id
        self.__student_id = student_id
        self.__grade_value = grade_value

    @property
    def discipline_id(self):
        return self.__discipline_id

    @discipline_id.setter
    def discipline_id(self, value):
        self.__discipline_id = value

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self, value):
        self.__student_id = value

    @property
    def grade_value(self):
        return self.__grade_value

    @grade_value.setter
    def grade_value(self, value):
        self.__grade_value = value

    def __str__(self):
        return str(
            "Discipline ID: {0} || Student ID: {1} || Grade: {2}".format(self.discipline_id, self.student_id,
                                                                         self.grade_value))


class Link(object):
    """
        Class that defines link entities
        constructor:
            Link(discipline_id, student_id)
        properties:
            discipline_id
            student_id
            link_id
        setters: -
        """
    def __init__(self, discipline_id, student_id):
        self.__discipline_id = discipline_id
        self.__student_id = student_id
        self.__link_id = str(discipline_id) + "." + str(student_id)

    @property
    def link_id(self):
        return self.__link_id

    @property
    def discipline_id(self):
        return self.__discipline_id

    @property
    def student_id(self):
        return self.__student_id

    def __str__(self):
        return "Student with ID {0} is enrolled at discipline with ID {1}".format(str(self.student_id),
                                                                                  str(self.discipline_id))
