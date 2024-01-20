import argparse

from src.managers import TeacherManager, StudentManager, SubjectManager, GradeManager, GroupManager

parser = argparse.ArgumentParser(description="CLI Application for CRUD operations with the database.")
parser.add_argument("--action", "-a", help="Command: create, remove, update, list")
parser.add_argument("--model", "-m", help="Model on which to perform the action.")
parser.add_argument("--name", "-n", help="Name for the new record or updated record.")
parser.add_argument("--id", type=int, help="ID of the record to update or remove.")
parser.add_argument("--group_id", type=int, help="Group ID for Student creation.")
parser.add_argument("--student_id", type=int, help="Student ID for Grade creation.")
parser.add_argument("--subject_id", type=int, help="Subject ID for Grade creation.")
parser.add_argument("--teacher_id", type=int, help="Teacher ID for Subject creation.")
parser.add_argument("--grade", type=int, help="Grade value for Grade creation.")

user_arg = parser.parse_args()
print(user_arg)

def main():
    managers = {
        "Teacher": TeacherManager(),
        "Group": GroupManager(),
        "Student": StudentManager(),
        "Subject": SubjectManager(),
        "Grade": GradeManager()
    }

    if user_arg.model not in managers:
        print(f"Invalid model: {user_arg.model}. Available models: {', '.join(managers.keys())}")
    
    manager = managers[user_arg.model]

    match user_arg.action:
        case "create":
            manager.create_(user_arg)

        case "update":
            manager.update_(user_arg)

        case "remove":
            manager.remove_(user_arg)

        case "list":
            manager.list_(user_arg)

        case _:
            print("Error")

if __name__ == "__main__":
    main()

    
