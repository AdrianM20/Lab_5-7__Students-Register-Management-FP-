"""
main Module

Created on 02.11.2016
@author adiM
"""

import traceback

from faculty.base_controllers.student_controller import StudentController
from faculty.base_controllers.discipline_controller import DisciplineController
from faculty.base_controllers.grade_controller import GradeController
from faculty.base_controllers.link_controller import LinkController
from faculty.base_controllers.statistics_controller import StatisticsController
from faculty.controllers_with_undo.discipline_undo_controller import DisciplineUndoController
from faculty.controllers_with_undo.grade_undo_controller import GradeUndoController
from faculty.controllers_with_undo.link_undo_controller import LinkUndoController
from faculty.controllers_with_undo.student_undo_controller import StudentUndoController
from faculty.repositories.student_repository import StudentRepository
from faculty.repositories.discipline_repository import DisciplineRepository
from faculty.repositories.grade_repository import GradeRepository
from faculty.repositories.link_repository import LinkRepository
from faculty.domain.validators import StudentValidator, DisciplineValidator, GradeValidator, LinkValidator, \
    FacultyException
from faculty.repositories.file_repository import StudentFileRepository, DisciplineFileRepository, \
    GradeFileRepository, LinkFileRepository, FileRepositoryException
from faculty.repositories.pickle_repository import StudentPickleRepository, DisciplinePickleRepository, \
    GradePickleRepository, LinkPickleRepository, PickleRepositoryException
from faculty.ui.console import Console
from faculty.controllers_with_undo.undo_controller import UndoController
from util.common import PropertiesLoader, RepositoriesChecker

if __name__ == "__main__":
    print()

    try:
        properties = PropertiesLoader.load_properties("../../src/settings.properties")

        """
        Initialize repositories as specified in the settings file, otherwise with None
        """
        grade_repository = None
        link_repository = None
        student_repository = None
        discipline_repository = None

        if properties["repository"] == "in memory":
            grade_repository = GradeRepository(GradeValidator)
            link_repository = LinkRepository(LinkValidator)
            student_repository = StudentRepository(StudentValidator)
            discipline_repository = DisciplineRepository(DisciplineValidator)
        elif properties["repository"] == "text file":
            grade_repository = GradeFileRepository(GradeValidator, properties["grades"])
            link_repository = LinkFileRepository(LinkValidator, properties["enrollments"])
            student_repository = StudentFileRepository(StudentValidator, properties["students"])
            discipline_repository = DisciplineFileRepository(DisciplineValidator, properties["disciplines"])
        elif properties["repository"] == "binary file":
            grade_repository = GradePickleRepository(GradeValidator, properties["grades"])
            link_repository = LinkPickleRepository(LinkValidator, properties["enrollments"])
            student_repository = StudentPickleRepository(StudentValidator, properties["students"])
            discipline_repository = DisciplinePickleRepository(DisciplineValidator, properties["disciplines"])

        """
        Initialize controllers and read data (if all the repositories are initialized correctly)
        """
        if RepositoriesChecker.check_all(student_repository, discipline_repository, grade_repository,
                                         link_repository):
            """
            Start undo controller
            """
            undo_controller = UndoController()

            """
            Start grade controller
            """
            grade_controller = GradeUndoController(undo_controller, grade_repository)

            """
            Start link controller
            """
            link_controller = LinkUndoController(undo_controller, link_repository)

            """
            Start student controller
            """
            student_controller = StudentUndoController(undo_controller, student_repository, grade_repository,
                                                       link_repository)

            """
            Start discipline controller
            """
            discipline_controller = DisciplineUndoController(undo_controller, discipline_repository,
                                                             grade_repository,
                                                             link_repository)

            """
            Start statistics controller
            """
            statistics_controller = StatisticsController(student_repository, discipline_repository,
                                                         grade_repository,
                                                         link_repository)

            """
            Start console
            """
            console = Console(undo_controller, student_controller, discipline_controller, grade_controller,
                              link_controller,
                              statistics_controller)

            console.run_console(properties["repository"])
        else:
            print("Program did not start because there was a problem when loading the repositories.")

    except FileRepositoryException as fre:
        print("Some files are missing or corrupted.")
        print("Please make sure that the following files are present and then restart the program:")
        print("\n", fre)
    except PickleRepositoryException as pre:
        print("Some files are missing or corrupted.")
        print("Please make sure that the following files are present and then restart the program:")
        print("\n", pre)
    except IOError as io:
        print("Some files are missing or corrupted.")
        print("Please make sure that all needed files are missing. "
              "If you don't know what is missing contact the programmer for help.")
        print("\n", io)
    except Exception as ex:
        print("Exception: ", ex)
        traceback.print_exc()

    print("\nBye")
