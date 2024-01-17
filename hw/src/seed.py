from faker import Faker
from src.conect_db import session
from src.models import Student, Teacher, Gruops, Grades, Subjects
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
    number = 1000
    start_date = datetime.strptime("2023-02-01", "%Y-%m-%d")
    end_date = datetime.strptime("2024-02-15", "%Y-%m-%d")

    def get_list_date(start: date, end: date):
        result = []
        current_data = start
        while current_data <= end:
            if current_data.isoweekday() < 6:
                result.append(current_data)
            current_data += timedelta(1)
        return result

    list_dates = get_list_date(start_date, end_date)

    student_id = [num for num in range(1, STUDENT + 1)]
    subjects_id = [num for num in range(1, len(SUBJECTS) + 1)]
    grades = [num for num in range(1, 13)]
    grades_of_student = {f"{el}" : 0 for el in range(1, STUDENT + 1)}
    
    while number > 0:
        for day_of in list_dates:
            n = 6
            for _ in range(1, n + 1):
                random_student = choice(student_id)
                random_subject = choice(subjects_id)
                random_grade = choice(grades)

                if grades_of_student[str(random_student)] < 20:
                    student_grade = Grades(
                        student_id = random_student,
                        subjects_id = random_subject,
                        grade = random_grade,
                        day = day_of
                    )
                    session.add(student_grade)
                    grades_of_student[str(random_student)] += 1
                    number -= 1
                else:
                    n += 1
    else:
        session.commit()

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
            address=fake.address(),
            gruop_id = randint(1, 3)
        )
        session.add(student)
    session.commit()


def main():
    pass
    create_students()
    create_teachers()
    create_groups(GRUOPS_NAME)
    create_subjects(SUBJECTS)
    create_grades()

# if __name__ == '__main__':
#     pass