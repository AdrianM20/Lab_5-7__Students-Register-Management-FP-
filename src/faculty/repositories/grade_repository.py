"""
grade_repository Module

Created on 07.11.2016
@author adiM
"""

from faculty.domain.validators import FacultyException


class GradeRepositoryException(FacultyException):
    pass


class GradeRepository(object):
    def __init__(self, validator_class):
        self.__validator_class = validator_class
        self._grades = []
        # self.__filename = filename

    def find_by_student(self, student_id):
        stud_grades = []
        for grd in self._grades:
            if grd.student_id == student_id:
                stud_grades.append(grd)
        if len(stud_grades) != 0:
            return stud_grades
        return None

    def find_by_discipline(self, discipline_id):
        dis_grades = []
        for grd in self._grades:
            if grd.discipline_id == discipline_id:
                dis_grades.append(grd)
        if len(dis_grades) != 0:
            return dis_grades
        return None

    def init_save(self, grade):
        self.__validator_class.validate(grade)
        self._grades.append(grade)

    def save(self, grade):
        self.__validator_class.validate(grade)
        self._grades.append(grade)
        # self.__save_to_file()

    def delete_by_student(self, student_id):
        if self.find_by_student(student_id) is not None:
            # raise GradeRepositoryException(
            #     "The student with the ID {0} did not receive any grade yet. Nothing was deleted".format(
            #         student_id))
            new_grades = []
            for grd in self._grades:
                if grd.student_id != student_id:
                    new_grades.append(grd)
            self._grades = new_grades
        # self.__save_to_file()

    def delete_by_discipline(self, discipline_id):
        if self.find_by_discipline(discipline_id) is not None:
            # raise GradeRepositoryException(
            #     "The discipline with ID {0} does not exist. Nothing was deleted".format(discipline_id))
            new_grades = []
            for grd in self._grades:
                if grd.discipline_id != discipline_id:
                    new_grades.append(grd)
            self._grades = new_grades
        # self.__save_to_file()

    def delete_specific_grade(self, grade):
        new_grades = []
        for grd in self._grades:
            if grd.discipline_id != grade.discipline_id or grd.student_id != grade.student_id or grd.grade_value != grade.grade_value:
                new_grades.append(grd)
        self._grades = new_grades
        # self.__save_to_file()

    def get_all(self):
        return self._grades

    def load_grades(self):
        pass

    def save_grades(self):
        pass
'''
    def __save_to_file(self):
        f = open(self.__filename, "w")
        try:
            for g in self.get_all():
                gString = str(g.discipline_id) + ", " + str(g.student_id) + ", " + str(g.grade_value) + "\n"
                f.write(gString)
            f.close()
        except Exception as e:
            print("An error occurred in file saving:")
            print(str(e))
'''