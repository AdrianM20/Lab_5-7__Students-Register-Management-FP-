"""
student_undo_controller Module

Created on 11.12.2016
@author adiM
"""
from faculty.base_controllers.student_controller import StudentController
from faculty.controllers_with_undo.undo_controller import FunctionCall, Operation
from faculty.domain.entities import Student


class StudentUndoController(StudentController):
    def __init__(self, undo_controller, student_repository, grade_repository, link_repository):
        StudentController.__init__(self, student_repository)
        self.__undo_controller = undo_controller
        self.__grade_repository = grade_repository
        self.__link_repository = link_repository

    def add_student(self, student_id, name):
        StudentController.add_student(self, student_id, name)

        self.__undo_controller.new_operation()
        redo = FunctionCall(self.add_student, student_id, name)
        undo = FunctionCall(self.remove_student, student_id)
        operation = Operation(redo, undo)
        self.__undo_controller.record_operation(operation)

    def remove_student(self, student_id):
        student = StudentController.find_by_id(self, student_id)
        links = self.__link_repository.find_by_student(student_id)
        grades = self.__grade_repository.find_by_student(student_id)
        StudentController.remove_student(self, student_id)

        self.__undo_controller.new_operation()
        redo = FunctionCall(self.remove_student, student_id)
        undo = FunctionCall(self.__restore_student_data, student_id, student.name, links, grades)
        operation = Operation(redo, undo)
        self.__undo_controller.record_operation(operation)

    def __restore_student_data(self, student_id, name, links, grades):
        StudentController.add_student(self,student_id,name)
        if links is not None:
            for link in links:
                self.__link_repository.save(link)
        if grades is not None:
            for grade in grades:
                self.__grade_repository.save(grade)

        self.__undo_controller.new_operation()
        redo = FunctionCall(self.__restore_student_data, student_id, name, links, grades)
        undo = FunctionCall(self.remove_student, student_id)
        operation = Operation(redo, undo)
        self.__undo_controller.record_operation(operation)

    def update_student(self, student_id, name):
        old_student = StudentController.find_by_id(self, student_id)
        StudentController.update_student(self, student_id, name)

        self.__undo_controller.new_operation()
        redo = FunctionCall(self.update_student, student_id, name)
        undo = FunctionCall(self.update_student, old_student.student_id, old_student.name)
        operation = Operation(redo, undo)
        self.__undo_controller.record_operation(operation)
