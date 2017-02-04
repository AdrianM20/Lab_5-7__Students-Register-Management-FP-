"""
statistics_controller Module

Created on 05.12.2016
@author adiM
"""
from faculty.domain.DTOs import StudentGradeDTO, StudentFailDTO, StudentAggregatedDTO, DisciplineAverageDTO


class StatisticsController(object):
    def __init__(self, student_repository, discipline_repository, grade_repository, link_repository):
        self.__student_repository = student_repository
        self.__discipline_repository = discipline_repository
        self.__grade_repository = grade_repository
        self.__link_repository = link_repository

    def average_discipline_grade_for_all(self, discipline_id):
        avg_grades = []
        for link in self.__link_repository.get_all():
            if link.discipline_id == discipline_id:
                student = self.__student_repository.find_by_id(link.student_id)
                average_grade = self.__discipline_average_grade(link.student_id, link.discipline_id)
                student_grade = StudentGradeDTO(student.name, average_grade)
                if average_grade is not None:
                    avg_grades.append(student_grade)
        return sorted(avg_grades, key=lambda stud_grade: stud_grade.avg_grade, reverse=True)

    def __discipline_average_grade(self, student_id, discipline_id):
        grades = []
        for grade in self.__grade_repository.get_all():
            if grade.student_id == student_id and grade.discipline_id == discipline_id:
                grades.append(grade.grade_value)
        sum_grades = sum(grades)
        if len(grades) == 0:
            return None
        return float(sum_grades) / len(grades)

    def failing_students(self):
        fails = []
        for discipline in self.__discipline_repository.get_all():
            for link in self.__link_repository.get_all():
                if link.discipline_id == discipline.discipline_id:
                    student = self.__student_repository.find_by_id(link.student_id)
                    average_grade = self.__discipline_average_grade(link.student_id, link.discipline_id)
                    student_fail = StudentFailDTO(student.name, discipline.name)
                    if average_grade is not None and average_grade < 5:
                        fails.append(student_fail)
        return fails

    def students_aggregated_grade(self):
        agr_averages = []
        for student in self.__student_repository.get_all():
            sum_of_avg = 0
            nr = 0
            for link in self.__link_repository.get_all():
                if link.student_id == student.student_id:
                    average_grade = self.__discipline_average_grade(link.student_id, link.discipline_id)
                    if average_grade is not None:
                        sum_of_avg += average_grade
                        nr += 1
            if sum_of_avg != 0:
                agr = float(sum_of_avg) / nr
                stud_aggr = StudentAggregatedDTO(student.name, agr)
                agr_averages.append(stud_aggr)
        return sorted(agr_averages, key=lambda aggreg: aggreg.aggreg_avg, reverse=True)

    def disciplines_averages(self):
        discipline_averages = []
        for discipline in self.__discipline_repository.get_all():
            sum_of_grades = 0
            nr_of_grades = 0
            for grade in self.__grade_repository.get_all():
                if grade.discipline_id == discipline.discipline_id:
                    sum_of_grades += grade.grade_value
                    nr_of_grades += 1
            if nr_of_grades != 0:
                avg = float(sum_of_grades) / nr_of_grades
                dis_avg = DisciplineAverageDTO(discipline.name, avg)
                discipline_averages.append(dis_avg)
        return sorted(discipline_averages, key=lambda dis_average: dis_average.avg_grade, reverse=True)
