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
    def create_(self, user_arg):
        print("create True")

    def update_(self, user_arg):
        print("update true")

    def remove_(self, user_arg):
        print("remove true")

    def list_(self, user_arg):
        print("list true")


class StudentManager(ModelsManager):
    def create_(self, user_arg):
        print("create True")

    def update_(self, user_arg):
        print("update true")

    def remove_(self, user_arg):
        print("remove true")

    def list_(self, user_arg):
        print("list true")


class GroupsManager(ModelsManager):
    def create_(self, user_arg):
        group = Groups(name = user_arg.name)
        session.add(group)
        session.commit()
        print(f"Created a group with the name {user_arg.name}")

    def update_(self, user_arg):
        group = session.query(Groups).get(user_arg.id)
        old_name = group.name
        group.name = user_arg.name
        session.add(group)
        session.commit()
        print(f"Group name updated {old_name} --> {user_arg.name}")

    def remove_(self, user_arg):
        group = session.query(Groups).get(user_arg.id)
        session.delete(group)
        session.commit()
        print(F"{group.name} group deleted")

    def list_(self, user_arg):
        group = session.query(Groups)
        for el in group:
            print(f"Group ID: {el.id} Group name: {el.name}")


class SubjectsManager(ModelsManager):
    def create_(self, user_arg):
        print("create True")

    def update_(self, user_arg):
        print("update true")

    def remove_(self, user_arg):
        print("remove true")

    def list_(self, user_arg):
        print("list true")


class GradesManager(ModelsManager):
    def create_(self, user_arg):
        print("create True")

    def update_(self, user_arg):
        print("update true")

    def remove_(self, user_arg):
        print("remove true")

    def list_(self, user_arg):
        print("list true")



