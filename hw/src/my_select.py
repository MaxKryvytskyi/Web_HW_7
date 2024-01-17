
from hw.src.models import Grades
from sqlalchemy import func
from hw.src.conect_db import session 

def select_1():
    average_grade = (
    session.query(func.avg(Grades.grade))
    .filter(Grades.student_id == 1, Grades.subjects_id == 1)
    .scalar()
    )

    print(f"Середнє значення оцінок: {average_grade}")

def select_2():
    pass

def select_3():
    pass

def select_4():
    pass

def select_5():
    pass

def select_6():
    pass

def select_7():
    pass

def select_8():
    pass

def select_9():
    pass

def select_10():
    pass

if __name__ == '__main__':
    # select_1()
    pass