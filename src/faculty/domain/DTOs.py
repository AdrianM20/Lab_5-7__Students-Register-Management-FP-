"""
DTOs Module

Created on 03.12.2016
@author adiM
"""


class StudentGradeDTO(object):
    """
        Class that defines student average grade for a discipline as DTO
        constructor:
            StudentGradeDTO(student_name, avg_grade)
        properties:
            student_name
            avg_grade
        setters:
            student_name
            avg_grade
        """
    def __init__(self, student_name, avg_grade):
        self.__student_name = student_name
        self.__avg_grade = avg_grade

    @property
    def student_name(self):
        return self.__student_name

    @student_name.setter
    def student_name(self, value):
        self.__student_name = value

    @property
    def avg_grade(self):
        return self.__avg_grade

    @avg_grade.setter
    def avg_grade(self, value):
        self.__avg_grade = value


class StudentFailDTO(object):
    """
        Class that defines a failing student for a discipline as DTO
        constructor:
            StudentFailDto(student_name, discipline_name)
        properties:
            student_name
            discipline_name
        setters:
            student_name
            discipline_name
        """
    def __init__(self, student_name, discipline_name):
        self.__student_name = student_name
        self.__discipline_name = discipline_name

    @property
    def student_name(self):
        return self.__student_name

    @student_name.setter
    def student_name(self, value):
        self.__student_name = value

    @property
    def discipline_name(self):
        return self.__discipline_name

    @discipline_name.setter
    def discipline_name(self, value):
        self.__discipline_name = value


class StudentAggregatedDTO(object):
    """
        Class that defines the aggregated average of a student as DTO
        constructor:
            StudentAggregatedDto(student_name, aggregated_average)
        properties:
            student_name
            aggregated_average
        setters:
            student_name
            aggregated_average
        """
    def __init__(self, student_name, aggregated_average):
        self.__student_name = student_name
        self.__aggregated_average = aggregated_average

    @property
    def student_name(self):
        return self.__student_name

    @student_name.setter
    def student_name(self, value):
        self.__student_name = value

    @property
    def aggreg_avg(self):
        return self.__aggregated_average

    @aggreg_avg.setter
    def aggreg_avg(self, value):
        self.__aggregated_average = value


class DisciplineAverageDTO(object):
    """
        Class that defines the average grade for a discipline as DTO
        constructor:
            DisciplineAverageDTO(discipline_name, average_grade)
        properties:
            discipline_name
            average_grade
        setters:
            discipline_name
            average_grade
        """
    def __init__(self, discipline_name, average_grade):
        self.__discipline_name = discipline_name
        self.__average_grade = average_grade

    @property
    def discipline_name(self):
        return self.__discipline_name

    @discipline_name.setter
    def discipline_name(self, value):
        self.__discipline_name = value

    @property
    def avg_grade(self):
        return self.__average_grade

    @avg_grade.setter
    def avg_grade(self, value):
        self.__average_grade = value
