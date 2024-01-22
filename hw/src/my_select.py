from sqlalchemy import func, desc

try:
    from models import Grade, Student, Subject, Group, Teacher
    from connect_db import session 
except ModuleNotFoundError:
    from src.models import Grade, Student, Subject, Group, Teacher
    from src.connect_db import session 


def select_1():
    # select AVG(grade), s.first_name, s.last_name, student_id
    # from grades
    # join students as s on student_id = s.id
    # GROUP by student_id, s.first_name, s.last_name
    # ORDER by AVG(grade) desc
    # limit 5
    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    
# Запит на отримання середнього балу, імені, прізвища та ідентифікатора студента
    results = (
        session.query(
            Student.full_name,
            Grade.student_id,
            func.avg(Grade.grade).label('average_grade')
        )
        .select_from(Grade)
        .join(Student, Grade.student_id == Student.id)
        .group_by(Student.id, Student.full_name, Grade.student_id)
        .order_by(desc('average_grade'))
        .limit(5)
        .all()
    )
    # Виведення результатів
    for result in results:
        print(f"Student ID: {result.student_id}")
        print(f"Name: {result.full_name}")
        print(f"Average Grade: {round(result.average_grade, 2)} \n")

def select_2():
    # select student_id, s.first_name, s.last_name, AVG(grade), s2.name
    # from grades
    # join students as s on student_id = s.id
    # join subjects as s2 on subjects_id = s2.id
    # where subjects_id = 1
    # GROUP by student_id, s.first_name, s.last_name, s2.name
    # ORDER by AVG(grade) desc
    # limit 1
    subject_id = 4
    # Знайти студента із найвищим середнім балом з певного предмета.
    results = (
        session.query(
            Grade.student_id,
            Student.full_name,
            func.avg(Grade.grade).label('average_grade'),
            Subject.name
        )
        .select_from(Grade)
        .join(Student, Grade.student_id == Student.id)
        .join(Subject, Subject.id == Grade.subject_id)
        .where(Subject.id == subject_id)
        .group_by(Student.id, Grade.student_id, Subject.name)
        .order_by(desc('average_grade'))
        .limit(1)
        .all()
    )
    # Виведення результатів
    for result in results:
        print(f"Student ID: {result.student_id}")
        print(f"Name: {result.full_name}")
        print(f"Average Grade: {round(result.average_grade, 2)}")
        print(f"Name subjects: {result.name}")

def select_3():
    # SELECT s.first_name, s.last_name, AVG(g.grade) AS average_grade, subjects.name AS subject_name, g2."name" 
    # FROM students AS s
    # JOIN grades AS g ON s.id = g.student_id
    # JOIN groups AS g2 ON g2.id = s.gruop_id 
    # JOIN subjects ON g.subjects_id = subjects.id
    # WHERE g2.id = 1 AND subjects.id = 1
    # GROUP BY g2.id, s.first_name, s.last_name, subjects.name, g2."name" 
    # ORDER BY average_grade DESC
    subject_id = 1
    group_id = 1
    # Знайти середній бал у групах з певного предмета.
    results = (
        session.query(
            Student.full_name,
            func.avg(Grade.grade).label('average_grade'),
            Subject.name.label('subject_name'),
            Group.name
        ).select_from(Student)
        .join(Grade, Student.id == Grade.student_id)
        .join(Group, Group.id == Student.group_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .where(Group.id == group_id, Grade.subject_id == subject_id)
        .group_by(Group.id, Subject.name, Group.name, Student.full_name)
        .order_by(desc('average_grade'))
        .all()
    )
    # Виведення результатів
    for result in results:
        print(f"Name: {result.full_name}")
        print(f"Average grade: {round(result.average_grade, 2)}")
        print(f"Name subjects: {result.subject_name}")
        print(f"Gruop name: {result.name} \n")

def select_4():
    # select AVG(g.grade) 
    # from grades as g 
    # Знайти середній бал на потоці (по всій таблиці оцінок).
    results = (
        session.query(
            func.avg(Grade.grade).label('average_grade')
        ).select_from(Grade)
        .all()
    )
    # Виведення результатів
    for result in results:
        print(f"Average Grade: {round(result.average_grade, 2)}")

def select_5():
    # select s."name" , t.first_name , t.last_name 
    # from subjects as s
    # join teachers as t on t.id = s.teacher_id  

    # Знайти які курси читає певний викладач.
    results = (
        session.query(
            Subject.name,
            Teacher.full_name
        ).select_from(Subject)
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .all()
    )

    # Виведення результатів
    for result in results:
        print(f"Name subjects: {result.name}")
        print(f"Name teacher: {result.full_name}\n")

def select_6():
    # SELECT s.first_name, s.last_name, g2."name" 
    # FROM students AS s
    # JOIN groups AS g2 ON g2.id = s.gruop_id 
    # WHERE g2.id = 1
    # GROUP BY s.first_name, s.last_name, g2."name" 

    group_id = 1
    # Знайти список студентів у певній групі.
    results = (
        session.query(
            Student.full_name,
            Group.name
        ).select_from(Student)
        .join(Group, Group.id == Student.group_id)
        .where(Group.id == group_id)
        .order_by(Student.full_name)
        .all()
    )

    # Виведення результатів
    for result in results:
        print(f"Name: {result.full_name}")
        print(f"Gruops name: {result.name}\n")

def select_7():
    # SELECT s.first_name, s.last_name, g.grade, subjects.name AS subject_name, g2."name" 
    # FROM students AS s
    # JOIN grades AS g ON s.id = g.student_id
    # JOIN groups AS g2 ON g2.id = s.gruop_id 
    # JOIN subjects ON g.subjects_id = subjects.id
    # WHERE g2.id = 1 AND subjects.id = 1
    # ORDER BY g.grade DESC

    subject_id = 1
    group_id = 1
    # Знайти оцінки студентів у окремій групі з певного предмета.
    results = (
        session.query(
            Student.full_name,
            Grade.grade,
            Subject.name.label("subject_name"),
            Group.name
        ).select_from(Student)
        .join(Grade, Grade.student_id == Student.id)
        .join(Group, Group.id == Student.group_id)
        .join(Subject, Grade.subject_id == Subject.id)
        .where(Group.id == group_id, Subject.id == subject_id)
        .order_by(desc(Grade.grade))
        .all()
    )

    # Виведення результатів
    for result in results:
        print(f"Name: {result.full_name}")
        print(f"Average Grade: {result.grade}")
        print(f"Subjects name: {result.subject_name}")
        print(f"Gruops name: {result.name}\n")

def select_8():
    # select t.first_name, t.last_name, s."name", AVG(g.grade) 
    # from subjects as s
    # join grades as g on g.subjects_id = s.id
    # join teachers as t on s.teacher_id = t.id  
    # where s.teacher_id = 1
    # group by t.first_name, t.last_name, s."name"

    teacher_id = 2
    # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    results = (
        session.query(
            Teacher.full_name,
            Subject.name,
            func.avg(Grade.grade).label("average_grade")
        )
        .select_from(Subject)
        .join(Grade, Grade.subject_id == Subject.id)
        .join(Teacher, Subject.teacher_id == Teacher.id)
        .where(Subject.teacher_id == teacher_id)
        .group_by(Teacher.full_name, Subject.name)
        .all()
    )
    if not results:
        print("No Teacher")
    else:
        # Виведення результатів
        for result in results:
            print(f"Teacher name: {result.full_name}")
            print(f"Subjects name: {result.name}")
            print(f"Average Grade: {result.average_grade} \n")

def select_9():
    # select s2."name", s.first_name, s.last_name 
    # from grades as g 
    # join subjects as s2 on s2.id = g.subjects_id 
    # join students as s on s.id = g.student_id  
    # where s.id = 1
    # group by s2."name", s.first_name, s.last_name  

    student_id = 1
    # Знайти список курсів, які відвідує певний студент.
    results = (
        session.query(
        Subject.name,
        Student.full_name
    )
    .select_from(Grade)
    .join(Subject, Subject.id == Grade.subject_id)
    .join(Student, Student.id == Grade.student_id)
    .where(Student.id == student_id)
    .group_by(Subject.name, Student.full_name)
    )

    # Виведення результатів
    print(f"Student name: {results[0].full_name}")
    for result in results:
        print(f"Subjects name: {result.name}")

def select_10():
    # select s2."name", s.first_name, s.last_name, t.first_name , t.last_name 
    # from grades as g 
    # join subjects as s2 on s2.id = g.subjects_id 
    # join students as s on s.id = g.student_id 
    # join teachers as t on t.id = s2.teacher_id 
    # where s.id = 1 and s2.teacher_id = 1
    # group by s2."name", s.first_name, s.last_name , t.first_name , t.last_name 
    
    student_id = 1
    teacher_id = 1
    # Список курсів, які певному студенту читає певний викладач.
    results = (
        session.query(
            Subject.name,
            Student.full_name.label("student_name"),
            Teacher.full_name.label("teacher_name"),
        )
        .select_from(Grade)
        .join(Subject, Subject.id == Grade.subject_id)
        .join(Student, Student.id == Grade.student_id)
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .where(Student.id == student_id, Subject.teacher_id == teacher_id)
        .group_by(Subject.name, Student.full_name, Teacher.full_name)
    )
    if not results:
        print("No teacher")
    else:
        # Виведення результатів
        print(f"Student name: {results[1].student_name}")
        print(f"Teacher name: {results[1].teacher_name}")
        for result in results:
            print(f"Subject name: {result.name}")
        
def select_11():
    # SELECT (s.first_name , s.last_name) as student_name , (t.first_name, t.last_name) as teacher_name, avg(g.grade) AS average_grade
    # FROM grades AS g
    # JOIN subjects AS s2 ON s2.id = g.subjects_id 
    # JOIN teachers AS t ON t.id = s2.teacher_id 
    # JOIN students AS s ON s.id = g.student_id
    # WHERE s.id = 1 AND t.id = 3
    # GROUP BY student_name , teacher_name
    
    student_id = 2
    teacher_id = 2
    # Середній бал, який певний викладач ставить певному студентові.
    results = (
        session.query(
            Teacher.full_name.label("teacher_name"),
            Student.full_name.label("student_name"),
            func.avg(Grade.grade).label("average_grade")
        )
        .select_from(Grade)
        .join(Subject, Subject.id == Grade.subject_id)
        .join(Student, Student.id == Grade.student_id)
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .where(Student.id == student_id, Teacher.id == teacher_id)
        .group_by(Student.full_name, Teacher.full_name)
        .all()
    )
    if not results:
        print("Not found")
    else:
        # Виведення результатів
        for result in results:
            print(f"Teacher name: {result.teacher_name}")
            print(f"Student name: {result.student_name}")
            print(f"Average Grade: {result.average_grade} \n")

def select_12():
    # SELECT g.name, s2.name, g2.grade, g2."day", s.first_name, s.last_name 
    # FROM "groups" AS g
    # JOIN students AS s ON s.gruop_id = g.id
    # JOIN grades AS g2 ON g2.student_id = s.id
    # JOIN subjects AS s2 ON s2.id = g2.subjects_id
    # WHERE g.id = 1 AND s2.id = 1
    # GROUP BY s.first_name, s.last_name, g.name, s2.name, g2.grade, g2."day"
    # order by "day" desc  
    # limit 1

    subject_id = 1
    group_id = 1

    # Оцінки студентів у певній групі з певного предмета на останньому занятті.
    results = (
        session.query(
            Group.name,
            Subject.name.label("subject_name"),
            Grade.grade,
            Grade.day,
            Student.full_name.label("student_name")
        )
        .select_from(Group)
        .join(Student, Student.group_id == Group.id)
        .join(Grade, Grade.student_id == Student.id)
        .join(Subject, Subject.id == Grade.subject_id)
        .where(Group.id == group_id, Subject.id == subject_id)
        .group_by(Student.full_name, Group.name, Subject.name, Grade.grade, Grade.day)
        .order_by(desc(Grade.day))
        .limit(1)
    )

    # Виведення результатів
    for result in results:
        print(f"Gruop name: {result.name}")
        print(f"Subject name: {result.subject_name}")
        print(f"Student name: {result.student_name}")
        print(f"Grade: {result.grade}")
        print(f"Date: {result.day} \n")

if __name__ == '__main__':
    select_1()
    # select_2()
    # select_3()
    # select_4()
    # select_5()
    # select_6()
    # select_7()
    # select_8()
    # select_9()
    # select_10()
    # select_11()
    # select_12()