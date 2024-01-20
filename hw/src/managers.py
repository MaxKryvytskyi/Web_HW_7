from sqlalchemy import desc
from datetime import datetime

try:
    from models import Student, Subject, Teacher, Grade, Group
    from connect_db import session
except ModuleNotFoundError:
    from src.models import Student, Subject, Teacher, Grade, Group
    from src.connect_db import session

class ModelsManager:
    def __init__(self) -> None:
        self.session = session

# +
class TeacherManager(ModelsManager):
    def create_(self, user_arg):
        fullname = user_arg.name.split()
        teacher = Teacher(first_name=fullname[0], last_name=fullname[1:][0], start_work=datetime.now())
        self.session.add(teacher)
        self.session.commit()
        print(f"A teacher with the name {user_arg.name}. Created")

    def update_(self, user_arg):
        teacher = self.session.query(Teacher).get(user_arg.teacher_id)
        fullname = user_arg.name.split()
        old_name = teacher.full_name
        teacher.first_name = fullname[0]
        teacher.last_name = fullname[1:][0]
        self.session.add(teacher)
        self.session.commit()
        print(f"Teacher name updated {old_name} --> {fullname[0]} {fullname[1:][0]}")

    def remove_(self, user_arg):
        teacher = self.session.query(Teacher).filter_by(id=user_arg.teacher_id).first()
        self.session.delete(teacher)
        self.session.commit()
        print(F"{teacher.full_name} teacher deleted")

    def list_(self, user_arg):
        teacher = self.session.query(Teacher)
        print("Teacher")
        for el in teacher:
            print(f"ID: {el.id} \nName: {el.full_name} \nWork: {el.start_work}\n")

# +
class StudentManager(ModelsManager):
    def create_(self, user_arg):
        fullname = user_arg.name.split()
        student = Student(first_name=fullname[0], last_name=fullname[1:][0], group_id=user_arg.group_id)
        self.session.add(student)
        self.session.commit()
        print(f"A student with the name {user_arg.name}. Created")

    def update_(self, user_arg):
        student = self.session.query(Student).get(user_arg.student_id)
        fullname = user_arg.name.split()
        old_name = student.full_name
        student.first_name = fullname[0]
        student.last_name = fullname[1:][0]
        self.session.add(student)
        self.session.commit()
        print(f"Student name updated {old_name} --> {fullname[0]} {fullname[1:][0]}")

    def remove_(self, user_arg):
        student = self.session.query(Student).filter_by(id=user_arg.student_id).first()
        self.session.delete(student)
        self.session.commit()
        print(F"{student.full_name} student deleted")

    def list_(self, user_arg):
        student = self.session.query(Student)
        for el in student:
            print(f"Student ID: {el.id} \nStudent name: {el.full_name}\n")

# +
class GroupManager(ModelsManager):
    def create_(self, user_arg):
        group = Group(name=user_arg.name)
        self.session.add(group)
        self.session.commit()
        print(f"Created a group with the name {user_arg.name}")

    def update_(self, user_arg):
        group = self.session.query(Group).get(user_arg.group_id)
        old_name = group.name
        group.name = user_arg.name
        self.session.add(group)
        self.session.commit()
        print(f"Group name updated {old_name} --> {user_arg.name}")

    def remove_(self, user_arg):
        group = self.session.query(Group).get(user_arg.group_id)
        self.session.delete(group)
        self.session.commit()
        print(F"{group.name} group deleted")

    def list_(self, user_arg):
        group = self.session.query(Group)
        for el in group:
            print(f"Group ID: {el.id} Group name: {el.name}")

# +
class SubjectManager(ModelsManager):
    def create_(self, user_arg):
        subject = Subject(name=user_arg.name, teacher_id=user_arg.teacher_id)
        self.session.add(subject)
        self.session.commit()
        print(f"Created subject")

    def update_(self, user_arg):
        subject = self.session.query(Subject).get(user_arg.subject_id)
        if user_arg.name:
            subject.name = user_arg.name
        if user_arg.teacher_id:
            subject.teacher_id = user_arg.teacher_id
        self.session.add(subject)
        self.session.commit()
        print(f"Subject name updated")

    def remove_(self, user_arg):
        subject = self.session.query(Subject).get(user_arg.subject_id)
        self.session.delete(subject)
        self.session.commit()
        print(F"Subject deleted")

    def list_(self, user_arg):
        subject = self.session.query(Subject)
        for el in subject:
            print(f"Subject ID: {el.id} Subject name: {el.name}")


class GradeManager(ModelsManager):
    def create_(self, user_arg):
        grade = Grade(grade=user_arg.grade, subject_id=user_arg.subject_id, student_id=user_arg.student_id)
        self.session.add(grade)               
        self.session.commit()
        print(f"Created grade")

    def update_(self, user_arg):
        grade = self.session.query(Grade).get(user_arg.id)
        if user_arg.subject_id:
            grade.subject_id = user_arg.subject_id
        if user_arg.student_id:
            grade.student_id = user_arg.student_id
        if user_arg.grade:
            grade.grade = user_arg.grade
        self.session.add(grade)
        self.session.commit()
        print(f"Grade updated")

    def remove_(self, user_arg):
        grade = self.session.query(Grade).get(user_arg.id)
        self.session.delete(grade)
        self.session.commit()
        print(F"Grade deleted")

    def list_(self, user_arg):
        grade = self.session.query(Grade)
        for el in grade:
            print(f"ID: {el.id} Subject ID: {el.subject_id} Student ID: {el.student_id} Grade: {el.grade} Date: {el.day}")



