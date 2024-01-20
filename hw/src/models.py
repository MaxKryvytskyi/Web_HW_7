from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

try:
    from connect_db import engine
except ModuleNotFoundError:
    from src.connect_db import engine

Base = declarative_base()

class Group(Base):
    __tablename__ = "group"
    id = Column(Integer, primary_key=True)
    name = Column(String(15))


class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=True)
    phone = Column(String(150), nullable=True)
    address = Column(String(150), nullable=True)
    start_work = Column(Date, nullable=False)
    student = relationship("Student", secondary="teacher_to_student", back_populates="teacher")

    @hybrid_property
    def full_name(self):
        return self.first_name + " " + self.last_name
              

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    email = Column(String(150), nullable=True)
    phone = Column(String(150), nullable=True)
    address = Column(String(150), nullable=True)
    group_id = Column(Integer, ForeignKey("group.id", ondelete="CASCADE"))
    group = relationship(Group)
    teacher = relationship("Teacher", secondary="teacher_to_student", back_populates="student")
    
    
    @hybrid_property
    def full_name(self):
        return self.first_name + " " + self.last_name


class TeacherStudent(Base):
    __tablename__ = "teacher_to_student"
    id = Column(Integer, primary_key=True)
    teacher_id = Column(Integer, ForeignKey("teacher.id", ondelete="CASCADE"))
    student_id = Column(Integer, ForeignKey("student.id", ondelete="CASCADE"))


class Subject(Base):
    __tablename__ = "subject"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey("teacher.id", ondelete="CASCADE"))
    teacher = relationship(Teacher)


class Grade(Base):
    __tablename__ = "grade"
    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey("subject.id", ondelete="CASCADE"))
    student_id = Column(Integer, ForeignKey("student.id", ondelete="CASCADE"))
    grade = Column(Integer)
    day = Column(Date)


Base.metadata.create_all(engine)





