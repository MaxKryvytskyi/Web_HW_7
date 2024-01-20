import argparse

from src.models import Student, Subjects, Teacher, Grades, Groups
from src.managers import TeacherManager, StudentManager, SubjectsManager, GradesManager, GroupsManager

parser = argparse.ArgumentParser(description="CLI Application for CRUD operations with the database.")
parser.add_argument("--action", "-a", help="Command: create, remove, update, list")
parser.add_argument("--model", "-m")
parser.add_argument("--name", "-n")
parser.add_argument("--id")
parser.add_argument("--desc")
parser.add_argument("--group_id")
parser.add_argument("--student_id")
parser.add_argument("--subject_id")
parser.add_argument("--teacher_id")

user_arg = parser.parse_args()
print(user_arg)

def main():
    managers = {
        "Teacher": TeacherManager(),
        "Group": GroupsManager(),
        "Student": StudentManager(),
        "Subject": SubjectsManager(),
        "Grade": GradesManager()
    }

    if user_arg.model not in managers:
        print(f"Invalid model: {user_arg.model}. Available models: {', '.join(managers.keys())}")
    
    manager = managers[user_arg.model]

    match user_arg.action:
        case "create":
            manager.create_(user_arg)
            print("create True")

        case "update":
            manager.update_(user_arg)
            print("update true")

        case "remove":
            manager.remove_(user_arg)
            print("remove true")

        case "list":
            manager.list_(user_arg)
            print("list true")

        case _:
            print("error")

if __name__ == "__main__":
    main()

    
