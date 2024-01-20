from sqlalchemy import desc
from datetime import datetime

try:
    from models import Student, Subjects, Teacher, Grades, Groups
    from connect_db import session
except ModuleNotFoundError:
    from src.models import Student, Subjects, Teacher, Grades, Groups
    from src.connect_db import session

class ModelsManager:
    def __init__(self) -> None:
        self.session = session


class TeacherManager(ModelsManager):
    def create_(self):
        pass

    def update_(self):
        pass

    def remove_(self):
        pass

    def list_(self):
        pass


class StudentManager(ModelsManager):
    def create_(self):
        pass

    def update_(self):
        pass

    def remove_(self):
        pass

    def list_(self):
        pass


class GroupsManager(ModelsManager):
    def create_(self):
        pass

    def update_(self):
        pass

    def remove_(self):
        pass

    def list_(self):
        pass 


class SubjectsManager(ModelsManager):
    def create_(self):
        pass

    def update_(self):
        pass

    def remove_(self):
        pass

    def list_(self):
        pass


class GradesManager(ModelsManager):
    def create_(self):
        pass

    def update_(self):
        pass

    def remove_(self):
        pass

    def list_(self):
        pass



