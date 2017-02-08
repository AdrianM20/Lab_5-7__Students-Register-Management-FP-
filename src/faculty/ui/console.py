"""
console Module

Created on 06.11.2016
@author adiM
"""

from faculty.domain.validators import FacultyException
from util.common import MyUtil


class Console(object):
    def __init__(self, undo_controller, student_controller, discipline_controller, grade_controller,
                 link_controller, statistics_controller):
        self.__undo_controller = undo_controller
        self.__student_controller = student_controller
        self.__discipline_controller = discipline_controller
        self.__grade_controller = grade_controller
        self.__link_controller = link_controller
        self.__statistics_controller = statistics_controller

    # ============================================== MAIN =========================================================

    def __data_init(self):
        self.__student_controller.add_student(1, "Mihai")
        self.__student_controller.add_student(2, "Alin")
        self.__student_controller.add_student(3, "Andrei")

        self.__discipline_controller.add_discipline(1, "OOP")
        self.__discipline_controller.add_discipline(2, "FP")
        self.__discipline_controller.add_discipline(3, "Web Development")

        self.__link_controller.add_link(1, 1)
        self.__link_controller.add_link(1, 2)
        self.__link_controller.add_link(1, 3)
        self.__link_controller.add_link(2, 1)
        self.__link_controller.add_link(3, 1)
        self.__link_controller.add_link(2, 3)

        self.__grade_controller.add_grade(1, 1, 10)
        self.__grade_controller.add_grade(1, 1, 6)
        self.__grade_controller.add_grade(1, 1, 7)
        self.__grade_controller.add_grade(1, 2, 3)
        self.__grade_controller.add_grade(1, 2, 9)
        self.__grade_controller.add_grade(1, 2, 8)
        self.__grade_controller.add_grade(1, 3, 5)
        self.__grade_controller.add_grade(1, 3, 7)
        self.__grade_controller.add_grade(1, 3, 8)

    def run_console(self, repo_type):
        options = {1: self.__student_menu,
                   2: self.__discipline_menu,
                   3: self.__grade_menu,
                   4: self.__statistics_menu,
                   5: self.__UI_print_enrollment,
                   6: self.__undo_LPO,
                   7: self.__redo_LPO}
        # self.__data_init()
        self.__greet_user(repo_type)
        while True:
            self.__main_menu()
            option = input("Enter option: ")
            if option == "x":
                break
            try:
                option = int(option)
                options[option]()
            except ValueError as ve:
                print("Invalid input", ve)
            except KeyError as ke:
                print("Option does not exist. Use one of the above", ke)
            except FacultyException as fe:
                print("An error occurred: ")
                print("Try again.")

                # try:
                #     self.__student_controller.add_student("s", "Marian")
                #     self.__student_controller.add_student(2, "Mihai")
                #     self.__student_controller.add_student(4, "Alin")
                # except FacultyException as fe:
                #     print("Error when adding students: ", fe)
                #     # traceback.print_exc()
                #
                # for stud in self.__student_controller.get_all():
                #     print(str(stud))

    @staticmethod
    def __main_menu():
        print("Please select an option:")
        print("\t1 - Student operations")
        print("\t2 - Discipline operations")
        print("\t3 - Grade operations")
        print("\t4 - Statistics menu")
        print("\t5 - Show enrollment")
        print("\t6 - Undo LPO")
        print("\t7 - Redo LPO")
        print("\tx - Exit program\n")

    def __UI_print_enrollment(self):
        for link in self.__link_controller.get_all():
            print(str(link))

    @staticmethod
    def __greet_user(repo_type):
        print("Students Register Management - version 2.8.1")
        if repo_type == "in memory":
            print("Program is running using in-memory repositories.")
        elif repo_type == "text file":
            print("Program is running using text file repositories.")
        elif repo_type == "binary file":
            print("Program is running using binary file repositories.")
        print("To perform any operation input a number corresponding to the list below.\n")

    def __undo_LPO(self):
        self.__undo_controller.undo()

    def __redo_LPO(self):
        self.__undo_controller.redo()

    # ============================================Student Operations===============================================

    def __student_menu(self):
        options = {1: self.__UI_add_student,
                   2: self.__UI_remove_student,
                   3: self.__UI_update_student,
                   4: self.__UI_enroll_student,
                   5: self.__UI_print_students,
                   6: self.__UI_search_students}
        while True:
            print("What would you like to do?")
            print("\t1 - Add student")
            print("\t2 - Remove student")
            print("\t3 - Update student")
            print("\t4 - Enroll student")
            print("\t5 - Print students")
            print("\t6 - Search students")
            print("\tx - Exit to main\n")

            option = input("Enter option:")
            if option == "x":
                break
            try:
                option = int(option)
                options[option]()
            except ValueError as ve:
                print("Invalid input", ve)
            except KeyError:
                print("Option does not exist. Use one of the above")
            except FacultyException as fe:
                print("Student operation error: ", fe)
                print("Try again.")

    def __UI_add_student(self):
        student_id = int(input("Student ID: "))
        name = input("Name: ")

        self.__student_controller.add_student(student_id, name)

    def __UI_remove_student(self):
        student_id = int(input("Student ID: "))

        self.__student_controller.remove_student(student_id)
        self.__link_controller.delete_student(student_id)
        self.__grade_controller.delete_student(student_id)

    def __UI_update_student(self):
        student_id = int(input("Student ID: "))
        name = input("Name: ")

        self.__student_controller.update_student(student_id, name)

    def __UI_enroll_student(self):
        student_id = int(input("Student ID: "))
        if self.__student_controller.find_by_id(student_id) is not None:
            discipline_id = int(input("Discipline ID: "))
            if self.__discipline_controller.find_by_id(discipline_id) is not None:
                self.__link_controller.add_link(discipline_id, student_id)
            else:
                print("This discipline does not exist. Try again")
        else:
            print("This student does not exist. Try again")

    def __UI_print_students(self):
        for stud in self.__student_controller.get_all():
            print(str(stud))

    def __UI_search_students(self):
        find = input("Enter a number or name for which you want to search the student: ")
        try:
            find = int(find)
            print(str(self.__student_controller.find_by_id(find)), "\n")
        except ValueError:
            # print("The given input cannot be used. Type a number or a name")
            if find.isalpha():
                prt = False
                for stud in self.__student_controller.get_all():
                    if MyUtil.match(find, stud.name):
                        print(str(stud))
                        prt = True
                if not prt:
                    print("There is no match")
            else:
                print("The input does not contain only letters")
            print("\n")

    # ===========================================Discipline Operations=============================================

    def __discipline_menu(self):
        options = {1: self.__UI_add_discipline,
                   2: self.__UI_remove_discipline,
                   3: self.__UI_update_discipline,
                   4: self.__UI_print_disciplines,
                   5: self.__UI_search_disciplines}

        while True:
            print("What would you like to do?")
            print("\t1 - Add discipline")
            print("\t2 - Remove discipline")
            print("\t3 - Update discipline")
            print("\t4 - Print disciplines")
            print("\t5 - Search disciplines")
            print("\tx - Exit to main\n")

            option = input("Enter option:")
            if option == "x":
                break
            try:
                option = int(option)
                options[option]()
            except ValueError as ve:
                print("Invalid input", ve)
            except KeyError:
                print("Option does not exist. Use one of the above")
            except FacultyException as fe:
                print("Discipline operation error: ", fe)
                print("Try again.")

    def __UI_add_discipline(self):
        discipline_id = int(input("Discipline ID: "))
        name = input("Name: ")

        self.__discipline_controller.add_discipline(discipline_id, name)

    def __UI_remove_discipline(self):
        discipline_id = int(input("Discipline ID: "))

        self.__discipline_controller.remove_discipline(discipline_id)
        self.__link_controller.delete_discipline(discipline_id)
        self.__grade_controller.delete_discipline(discipline_id)

    def __UI_update_discipline(self):
        discipline_id = int(input("Discipline ID: "))
        name = input("Name: ")

        self.__discipline_controller.update_discipline(discipline_id, name)

    def __UI_print_disciplines(self):
        for dis in self.__discipline_controller.get_all():
            print(str(dis))

    def __UI_search_disciplines(self):
        find = input("Enter a number or name for which you want to search the disciplines: ")
        try:
            find = int(find)
            print(str(self.__discipline_controller.find_by_id(find)), "\n")
        except ValueError:
            if find.isalpha():
                prt = False
                for dis in self.__discipline_controller.get_all():
                    if MyUtil.match(find, dis.name):
                        print(str(dis))
                        prt = True
                if not prt:
                    print("There is no match")
            else:
                print("The input does not contain only letters")
            print("\n")

    # ===========================================Grade Operations==================================================

    def __grade_menu(self):
        options = {1: self.__UI_add_grade,
                   2: self.__UI_print_grades}

        while True:
            print("What would you like to do?")
            print("\t1 - Add Grade")
            print("\t2 - Show grades")
            print("\tx - Exit to main\n")

            option = input("Enter option:")
            if option == "x":
                break
            try:
                option = int(option)
                options[option]()
            except ValueError as ve:
                print("Invalid input", ve)
            except KeyError:
                print("Option does not exist. Use one of the above")
            except FacultyException as fe:
                print("Grade operation error: ", fe)
                print("Try again.")

    def __UI_add_grade(self):
        discipline_id = int(input("Discipline ID: "))
        if self.__discipline_controller.find_by_id(discipline_id) is not None:
            student_id = int(input("Student ID: "))
            if self.__student_controller.find_by_id(student_id) is not None:
                link_id = str(discipline_id) + "." + str(student_id)
                if self.__link_controller.find_by_id(link_id) is not None:
                    grade_value = int(input("Grade: "))

                    self.__grade_controller.add_grade(discipline_id, student_id, grade_value)
                else:
                    print("The student with the given ID is not enrolled at the given discipline.")
            else:
                print("There is no student with this ID.")
        else:
            print("There is no discipline with this ID.")

    def __UI_print_grades(self):
        for grd in self.__grade_controller.get_all():
            print(str(grd))

    # ===============================================Statistics====================================================

    def __statistics_menu(self):
        options = {1: self.__statistic1,
                   2: self.__statistic2,
                   3: self.__statistic3,
                   4: self.__statistic4}

        while True:
            print("\nChoose the statistics you want to see:")
            print("\t1 - Show students enrolled at a given discipline sorted by descending order of average grade")
            print("\t2 - Show all students failing at one or more disciplines")
            print("\t3 - Students with the best school situation, "
                  "sorted in descending order of their aggregated average")
            print("\t4 - All disciplines at which there is at least one grade, "
                  "sorted in descending order of the average grade received by all students")
            print("\tx - Exit to main\n")

            option = input("Enter option: ")
            if option == "x":
                break
            try:
                option = int(option)
                options[option]()
            except ValueError as ve:
                print("Invalid input:", ve)
            except KeyError:
                print("Option does not exist. Use one of the above")
            except FacultyException as fe:
                print("Statistics error: ", fe)
                print("Try again.")

    def __statistic1(self):
        try:
            discipline_id = int(input("Discipline ID: "))
            if self.__discipline_controller.find_by_id(discipline_id) is None:
                raise FacultyException("The given discipline id does not exist.")
        except ValueError:
            raise ValueError("Discipline ID should be an natural number")

        discipline_grades = self.__statistics_controller.average_discipline_grade_for_all(discipline_id)
        if len(discipline_grades) != 0:
            print("The average grades for discipline {0} are the following:\n".format(
                self.__discipline_controller.find_by_id(discipline_id).name))
            for grade in discipline_grades:
                print("Student name: {0} || Grade {1:0.2f}".format(grade.student_name, grade.avg_grade))
        else:
            print("No students received grades at {0}.\n".format(
                self.__discipline_controller.find_by_id(discipline_id).name))

    def __statistic2(self):
        fails = self.__statistics_controller.failing_students()
        if len(fails) != 0:
            print("The students that are failing are:\n")
            for fail in fails:
                print("{0} is failing at {1}".format(fail.student_name, fail.discipline_name))
        else:
            print("There are no students failing. Nice!\n")

    def __statistic3(self):
        print("Students with the best school situation:\n")
        aggreg_avg = self.__statistics_controller.students_aggregated_grade()
        for grade in aggreg_avg:
            print("{0} has an aggregated average of {1:0.2f}".format(grade.student_name, grade.aggreg_avg))

    def __statistic4(self):
        disciplines_average = self.__statistics_controller.disciplines_averages()
        if len(disciplines_average):
            print("The averages for each discipline are:\n")
            for avg in disciplines_average:
                print("{0} has an average grade of {1:0.2f}".format(avg.discipline_name, avg.avg_grade))
        else:
            print("No grades have been given at any discipline\n")
