import argparse
from random import choice

from src.managers import TeacherManager, StudentManager, SubjectsManager, GradesManager, GroupsManager
from src.seed import main
from src.my_select import select_1 

parser = argparse.ArgumentParser(description="CLI Application for CRUD operations with the database.")
parser.add_argument("--action", "-a", help="Command: create, remove, update, list")
parser.add_argument("--model", "-m")
parser.add_argument("--name", "-n")
parser.add_argument("--id")
parser.add_argument("--desc")

user_arg = parser.parse_args()

print(user_arg.id)

def main():
    managers = {
        "Teacher": TeacherManager(),
        "Group": GroupsManager(),
        "Student": StudentManager(),
        "Subject": SubjectsManager(),
        "Grade": GradesManager(),

    }
    if user_arg.model not in managers:
        print(f"Invalid model: {user_arg.model}. Available models: {', '.join(managers.keys())}")
    manager = managers[user_arg.model]
    
    print(manager)

    match user_arg.action:
        case "create":
            print("create True")
        case "remove":
            print("remove true")
        case "update":
            print("update true")
        case "list":
            print("list true")
        case "_":
            print("error")

if __name__ == "__main__":
    main()

    
