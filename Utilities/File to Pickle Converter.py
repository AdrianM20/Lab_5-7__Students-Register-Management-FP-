"""
File to Pickle Converter Module

Created on 09.01.2017
@author adiM
"""

from src.faculty.repositories.file_repository import StudentFileRepository, DisciplineFileRepository, \
    LinkFileRepository, GradeFileRepository
from src.faculty.repositories.pickle_repository import StudentPickleRepository, DisciplinePickleRepository, \
    LinkPickleRepository, GradePickleRepository
from src.faculty.domain.validators import StudentValidator, DisciplineValidator, LinkValidator, GradeValidator

if __name__ == "__main__":
    print()
    """"""
    s1 = StudentFileRepository(StudentValidator, "../data/students")
    s1.load_students()

    s2 = StudentPickleRepository(StudentValidator, "../pickles/students.pickle")
    s2.load_students()
    # s2._students = s1._students
    # s2.save_students()
    """"""
    s1 = DisciplineFileRepository(DisciplineValidator, "../data/disciplines")
    s1.load_disciplines()

    s2 = DisciplinePickleRepository(DisciplineValidator, "../pickles/disciplines.pickle")
    s2.load_disciplines()
    # s2._disciplines = s1._disciplines
    # s2.save_disciplines()
    """"""
    s1 = LinkFileRepository(LinkValidator, "../data/enrollment")
    s1.load_enrollment()

    s2 = LinkPickleRepository(LinkValidator, "../pickles/enrollment.pickle")
    s2.load_enrollment()
    # s2._links = s1._links
    # s2.save_enrollment()
    """"""
    s1 = GradeFileRepository(GradeValidator, "../data/grades")
    s1.load_grades()

    s2 = GradePickleRepository(GradeValidator, "../pickles/grades.pickle")
    s2.load_grades()
    # s2._grades = s1._grades
    # s2.save_grades()
    """"""
    print("Done!")
