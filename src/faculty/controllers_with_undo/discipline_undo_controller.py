"""
discipline_undo_controller Module

Created on 11.12.2016
@author adiM
"""
from faculty.base_controllers.discipline_controller import DisciplineController
from faculty.controllers_with_undo.undo_controller import FunctionCall, Operation


class DisciplineUndoController(DisciplineController):
    def __init__(self, undo_controller, discipline_repository, grade_repository, link_repository):
        DisciplineController.__init__(self, discipline_repository)
        self.__undo_controller = undo_controller
        self.__grade_repository = grade_repository
        self.__link_repository = link_repository

    def add_discipline(self, discipline_id, name):
        DisciplineController.add_discipline(self, discipline_id, name)

        self.__undo_controller.new_operation()
        redo = FunctionCall(self.add_discipline, discipline_id, name)
        undo = FunctionCall(self.remove_discipline, discipline_id)
        operation = Operation(redo, undo)
        self.__undo_controller.record_operation(operation)

    def remove_discipline(self, discipline_id):
        discipline = DisciplineController.find_by_id(self, discipline_id)
        links = self.__link_repository.find_by_discipline(discipline_id)
        grades = self.__grade_repository.find_by_discipline(discipline_id)
        DisciplineController.remove_discipline(self, discipline_id)

        self.__undo_controller.new_operation()
        redo = FunctionCall(self.remove_discipline, discipline_id)
        undo = FunctionCall(self.__restore_discipline_data, discipline_id, discipline.name, links, grades)
        operation = Operation(redo, undo)
        self.__undo_controller.record_operation(operation)

    def __restore_discipline_data(self, discipline_id, name, links, grades):
        DisciplineController.add_discipline(self, discipline_id,name)
        if links is not None:
            for link in links:
                self.__link_repository.save(link)
        if grades is not None:
            for grade in grades:
                self.__grade_repository.save(grade)

        self.__undo_controller.new_operation()
        redo = FunctionCall(self.__restore_discipline_data, discipline_id, name, links, grades)
        undo = FunctionCall(self.remove_discipline, discipline_id)
        operation = Operation(redo, undo)
        self.__undo_controller.record_operation(operation)

    def update_discipline(self, discipline_id, name):
        old_discipline = DisciplineController.find_by_id(self, discipline_id)
        DisciplineController.update_discipline(self, discipline_id, name)

        self.__undo_controller.new_operation()
        redo = FunctionCall(self.update_discipline, discipline_id, name)
        undo = FunctionCall(self.update_discipline, old_discipline.discipline_id, old_discipline.name)
        operation = Operation(redo, undo)
        self.__undo_controller.record_operation(operation)
