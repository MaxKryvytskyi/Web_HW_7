
from models import Grades
from sqlalchemy import func
from conect_db import session 

def select_1():
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    average_grade = (
    session.query(func.avg(Grades.grade))
    .filter(Grades.student_id == 1, Grades.subjects_id == 1)
    .scalar()
    )

    print(f"Середнє значення оцінок: {average_grade}")

def select_2():
    # Знайти студента із найвищим середнім балом з певного предмета.
    pass

def select_3():
    # Знайти середній бал у групах з певного предмета.
    pass

def select_4():
    # Знайти середній бал на потоці (по всій таблиці оцінок).
    pass

def select_5():
    # Знайти які курси читає певний викладач.
    pass

def select_6():
    # Знайти список студентів у певній групі.
    pass

def select_7():
    # Знайти оцінки студентів у окремій групі з певного предмета.
    pass

def select_8():
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    pass

def select_9():
    # Знайти список курсів, які відвідує певний студент.
    pass

def select_10():
    # Список курсів, які певному студенту читає певний викладач.
    pass

if __name__ == '__main__':
    # select_1()
    pass