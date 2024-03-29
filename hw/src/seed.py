from faker import Faker
from random import randint, choice
from datetime import datetime, date, timedelta
from sqlalchemy.orm import aliased

try:
    from connect_db import session
    from models import Student, Teacher, Group, Grade, Subject, TeacherStudent
except ModuleNotFoundError:
    from src.connect_db import session
    from src.models import Student, Teacher, Group, Grade, Subject, TeacherStudent


STUDENT = 50
TEACHER = 5
GROUPS_NAME = ["Space-T43", "Sparta-F23", "Vavilon-D10"]
SUBJECTS = ["Англійська",
            "Програмування",
            "Теорія імовірності",
            "Лінійна Алгебра",
            "Вища математика",
            "Дискретна математика",
            "SQL Запити",
            "Бази данних"]

fake = Faker('uk-UA')

def create_groups(groups_name):
    for group_name in groups_name:
        gruop = Group(
            name = group_name
        )
        session.add(gruop)
    session.commit()
    print("Group +")

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
    print("Teacher +")

def create_subjects(subjects_name):
    for subject_name in subjects_name:
        subject = Subject(
            name = subject_name,
            teacher_id = randint(1, TEACHER)
        )
        session.add(subject)
    session.commit()
    print("Subject +")

def create_students():
    for _ in range(1, STUDENT + 1):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.ascii_free_email(),
            phone=fake.phone_number(),
            address=fake.address(),
            group_id = randint(1, 3)
        )
        session.add(student)
    session.commit()
    print("Student +")

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
    subject_id = [num for num in range(1, len(SUBJECTS) + 1)]
    grades = [num for num in range(1, 13)]
    grades_of_student = {f"{el}" : 0 for el in range(1, STUDENT + 1)}
    
    while number > 0:
        for day_of in list_dates:
            n = 6
            for _ in range(1, n + 1):
                random_student = choice(student_id)
                random_subject = choice(subject_id)
                random_grade = choice(grades)

                if grades_of_student[str(random_student)] < 20:
                    student_grade = Grade(
                        student_id = random_student,
                        subject_id = random_subject,
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
        print("Grade +")

def create_teachers_to_students():
    # Створення аліасу для моделі Teacher
    teacher_alias = aliased(Teacher)
    result = []
    # Запит через ORM
    for student in range(1, STUDENT + 1):
        result.append((
            session.query(Grade.student_id, teacher_alias.id.label('teacher_id'))
            .join(Subject, teacher_alias.id == Subject.teacher_id)
            .join(Grade, Subject.id == Grade.subject_id)
            .filter_by(student_id=student)
            .distinct()
            .order_by(teacher_alias.id)
            .all()
        ))
    # Виведення результатів
    for el in result:
        for row in el: 
            # print(f"Teacher ID: {row.teacher_id}, Student ID: {row.student_id}")
            teacher_student = TeacherStudent(teacher_id=row.teacher_id, student_id=row.student_id)
            session.add(teacher_student)
    session.commit()
    print("Teacher To Student +")

def main():
    create_groups(GROUPS_NAME)
    create_teachers()
    create_subjects(SUBJECTS)
    create_students()
    create_grades()
    create_teachers_to_students()

if __name__ == '__main__':
    main()
