"""
undo_controller Module

Created on 11.12.2016
@author adiM
"""


class UndoController:
    def __init__(self):
        self.__operations = []
        self.__index = -1
        self.__redo_counter = 0
        self.__recorded = True

    @property
    def steps(self):
        return len(self.__operations)

    def record_operation(self, operation):
        if self.isRecorded() is True:
            self.__operations[-1].append(operation)

    def new_operation(self):
        if self.isRecorded() is False:
            return

        self.__operations = self.__operations[0:self.__index + 1]
        self.__operations.append([])
        self.__index += 1

    def isRecorded(self):
        return self.__recorded

    def undo(self):
        if self.__index < 0:
            print("No more undo possibility\n")
            return False

        self.__recorded = False

        for oper in self.__operations[self.__index]:
            oper.undo()

        self.__recorded = True

        self.__index -= 1
        self.__redo_counter += 1
        return True

    def redo(self):
        if self.__redo_counter < 1:
            print("No more redo possibility.\n")
            return False

        self.__recorded = False

        for oper in self.__operations[self.__index + 1]:
            oper.redo()

        self.__recorded = True

        self.__index += 1
        self.__redo_counter -= 1
        return True


class FunctionCall:
    def __init__(self, functionRef, *parameters):
        self.__functionRef = functionRef
        self.__parameters = parameters

    def call(self):
        self.__functionRef(*self.__parameters)


class Operation:
    def __init__(self, functionDo, functionUndo):
        self.__functionDo = functionDo
        self.__functionUndo = functionUndo

    def undo(self):
        self.__functionUndo.call()

    def redo(self):
        self.__functionDo.call()
