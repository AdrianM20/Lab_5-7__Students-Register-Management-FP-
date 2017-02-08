"""
link_repository Module

Created on 20.11.2016
@author adiM
"""
from copy import deepcopy

from faculty.domain.validators import FacultyException


class LinkRepositoryException(FacultyException):
    pass


class LinkRepository(object):
    def __init__(self, validator_class):
        self.__validator_class = validator_class
        self._links = {}
        # self.__filename = filename

    def find_link(self, link_id):
        if link_id in self._links:
            return self._links[link_id]
        return None

    def find_by_student(self, student_id):
        stud_links = []
        for link in self._links.values():
            if link.student_id == student_id:
                stud_links.append(link)
        if len(stud_links) != 0:
            return stud_links
        return None

    def find_by_discipline(self, discipline_id):
        dis_links = []
        for link in self._links.values():
            if link.discipline_id == discipline_id:
                dis_links.append(link)
        if len(dis_links) != 0:
            return dis_links
        return None

    def init_save(self, link):
        if self.find_link(link.link_id) is not None:
            raise LinkRepositoryException("Student is already enrolled at this discipline")
        self.__validator_class.validate(link)
        self._links[link.link_id] = link

    def save(self, link):
        if self.find_link(link.link_id) is not None:
            raise LinkRepositoryException("Student is already enrolled at this discipline")
        self.__validator_class.validate(link)
        self._links[link.link_id] = link
        # self.__save_to_file()

    def delete_by_student(self, student_id):
        links = deepcopy(self._links)
        for link in links.values():
            if link.student_id == student_id:
                del self._links[link.link_id]
                # self.__save_to_file()

    def delete_by_discipline(self, discipline_id):
        links = deepcopy(self._links)
        for link in links.values():
            if link.discipline_id == discipline_id:
                del self._links[link.link_id]
                # self.__save_to_file()

    def delete_specific_link(self, link_id):
        del self._links[link_id]
        # self.__save_to_file()

    def get_all(self):
        return self._links.values()

    def load_enrollment(self):
        pass

    def save_enrollment(self):
        pass


'''
    def __save_to_file(self):
        f = open(self.__filename, "w")
        try:
            for l in self.get_all():
                lString = str(l.discipline_id) + ", " + str(l.student_id) + "\n"
                f.write(lString)
            f.close()
        except Exception as e:
            print("An error occurred in file saving:")
            print(str(e))
'''
