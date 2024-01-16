from faker import Faker
from ..src.conect_db import session
from ..src.models import Student, Teacher, Gruops, Grades, Subjects
from random import randint, choice
from datetime import datetime, date, timedelta



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
    student_id = [num for num in range(1, STUDENT + 1)]
    subjects_id = [num for num in range(1, SUBJECTS + 1)]
    grades = [num for num in range(1, 13)]
    n = STUDENT
    while n > 0:
        random_student = choice(student_id)
        student_id.remove(random_student)
        for _ in range(1, 21):
            random_subjects = choice(subjects_id)
            random_grades = choice(grades)
            random_student






    # start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    # end_date = datetime.strptime("2023-06-15", "%Y-%m-%d")

    # def get_list_date(start: date, end: date):
    #     result = []
    #     current_data = start
    #     while current_data <= end:
    #         if current_data.isoweekday() < 6:
    #             result.append(current_data)
    #         current_data += timedelta(1)
    #     return result

    # list_dates = get_list_date(start_date, end_date)
    # grades = []

    # subjects = session.query(Subjects).all()
    # students = session.query(Student).all()

    # for day in list_dates:
    #     random_subject = choice(subjects)
    #     random_student = choice(students)

    #     grades.append(Grades(subjects_id=random_subject.id,
    #                         student_id=random_student.id, grade=randint(1, 12), day=day.date()))

    # session.add_all(grades)
    # session.commit()

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
    # create_students()
    # create_teachers()
    # create_groups(GRUOPS_NAME)
    # create_subjects(SUBJECTS)

if __name__ == '__main__':
    pass