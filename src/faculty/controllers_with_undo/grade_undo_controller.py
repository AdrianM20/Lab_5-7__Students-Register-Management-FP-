"""
grade_undo_controller Module

Created on 12.12.2016
@author adiM
"""
from faculty.base_controllers.grade_controller import GradeController
from faculty.controllers_with_undo.undo_controller import FunctionCall, Operation
from faculty.domain.entities import Grade


class GradeUndoController(GradeController):
    def __init__(self, undo_controller, grade_repository):
        GradeController.__init__(self, grade_repository)
        self.__undo_controller = undo_controller

    def add_grade(self, discipline_id, student_id, grade_value):
        GradeController.add_grade(self, discipline_id, student_id, grade_value)

        self.__undo_controller.new_operation()
        redo = FunctionCall(self.add_grade, discipline_id, student_id, grade_value)
        undo = FunctionCall(self.delete_grade, discipline_id, student_id, grade_value)
        operation = Operation(redo, undo)
        self.__undo_controller.record_operation(operation)

    def delete_grade(self, discipline_id, student_id, grade_value):
        GradeController.delete_grade(self, discipline_id, student_id, grade_value)

        self.__undo_controller.new_operation()
        redo = FunctionCall(self.delete_grade, discipline_id, student_id, grade_value)
        undo = FunctionCall(self.add_grade, discipline_id, student_id, grade_value)
        operation = Operation(redo, undo)
        self.__undo_controller.record_operation(operation)
