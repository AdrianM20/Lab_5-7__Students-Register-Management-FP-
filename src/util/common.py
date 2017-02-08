"""
common Module

Created on 02.12.2016
@author adiM
"""


class MyUtil(object):
    @staticmethod
    def match(s, t):
        s = s.lower()
        t = t.lower()
        return s in t


class PropertiesLoader(object):
    @staticmethod
    def load_properties(filepath, sep='=', comment_char='#'):
        """
        Read the file passed as parameter as a properties file
        """
        properties = {}
        with open(filepath, 'rt') as f:
            for line in f:
                l = line.strip()
                if l and not l.startswith(comment_char):
                    key_value = l.split(sep)
                    key = key_value[0].strip()
                    value = sep.join(key_value[1:]).strip().strip('"')
                    properties[key] = value
        return properties


class RepositoriesChecker(object):
    @staticmethod
    def check_all(student_repo, discipline_repo, grade_repo, link_repo):
        if student_repo is None:
            return False
        if discipline_repo is None:
            return False
        if grade_repo is None:
            return False
        if link_repo is None:
            return False
        return True
