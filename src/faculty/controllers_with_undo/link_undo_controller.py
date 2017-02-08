"""
link_undo_controller Module

Created on 12.12.2016
@author adiM
"""
from faculty.base_controllers.link_controller import LinkController
from faculty.controllers_with_undo.undo_controller import Operation, FunctionCall
from faculty.domain.entities import Link


class LinkUndoController(LinkController):
    def __init__(self, undo_controller, link_repository):
        LinkController.__init__(self, link_repository)
        self.__undo_controller = undo_controller

    def add_link(self, discipline_id, student_id):
        LinkController.add_link(self, discipline_id, student_id)
        link = Link(discipline_id, student_id)

        self.__undo_controller.new_operation()
        redo = FunctionCall(self.add_link, discipline_id, student_id)
        undo = FunctionCall(self.delete_link, link.link_id)
        operation = Operation(redo, undo)
        self.__undo_controller.record_operation(operation)

    def delete_link(self, link_id):
        link = LinkController.find_by_id(self, link_id)
        LinkController.delete_link(self, link_id)

        self.__undo_controller.new_operation()
        redo = FunctionCall(self.delete_link, link_id)
        undo = FunctionCall(self.add_link, link.discipline_id, link.student_id)
        operation = Operation(redo, undo)
        self.__undo_controller.record_operation(operation)
