from sqlalchemy import  Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
try:
    from src.conect_db import engine
except ModuleNotFoundError:
    from conect_db import engine
Base = declarative_base()


class Groups(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(15))


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    phone = Column(String(150), nullable=False)
    address = Column(String(150), nullable=False)
    start_work = Column(Date, nullable=False)
    students = relationship("Student", secondary="teachers_to_students", back_populates="teachers")

    @hybrid_property
    def full_name(self):
        return self.first_name + " " + self.last_name
              

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    phone = Column(String(150), nullable=False)
    address = Column(String(150), nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id", ondelete="CASCADE"))
    groups = relationship(Groups)
    teachers = relationship("Teacher", secondary="teachers_to_students", back_populates="students")
    
    
    @hybrid_property
    def full_name(self):
        return self.first_name + " " + self.last_name


class TeacherStudent(Base):
    __tablename__ = "teachers_to_students"
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey("teachers.id", ondelete="CASCADE"))
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))


class Subjects(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey("teachers.id", ondelete="CASCADE"))
    teacher = relationship(Teacher)

class Grades(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    subjects_id = Column(Integer, ForeignKey("subjects.id", ondelete="CASCADE"))
    student_id = Column(Integer, ForeignKey("students.id", ondelete="CASCADE"))
    grade = Column(Integer)
    day = Column(Date)

Base.metadata.create_all(engine)





