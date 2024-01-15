from faker import Faker
from ..src.conect_db import session
from ..src.models import Student, Teacher, Gruops, Grades, Subjects
from random import randint



STUDENT = 50
TEACHER = 5
GRUOPS_NAME = ["Space - T43", "Sparta - F23", "Vavilon - D10"]
SUBJECTS = ["Англійська",
            "Програмування",
            "Теорія імовірності",
            "Лінійна Алгебра",
            "Вища математика",
            "Дискретна математика",
            "SQL Запити",
            "Бази данних"]

fake = Faker('uk-UA')

def create_grades():
    pass

def create_subjects(subjects_name):
    for subject in subjects_name:
        subjects = Subjects(
            name = subject,
            teacher_id = randint(1, TEACHER)
        )
        session.add(subjects)
    session.commit()

def create_groups(groups_name):
    for gruop_name in groups_name:
        gruops = Gruops(
            name = gruop_name
        )
        session.add(gruops)
    session.commit()

def create_teachers():
    for _ in range(1, TEACHER + 1):
        teacher = Teacher(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            phone=fake.phone_number(),
            address=fake.address(),
            start_work=fake.date_between(start_date='-5y')
        )
        session.add(teacher)
    session.commit()


def create_students():
    for _ in range(1, STUDENT + 1):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            phone=fake.phone_number(),
            address=fake.address()
        )
        session.add(student)
    session.commit()


def main():
    create_grades()
    create_students()
    create_teachers()
    create_groups(GRUOPS_NAME)
    create_subjects(SUBJECTS)

if __name__ == '__main__':
    pass