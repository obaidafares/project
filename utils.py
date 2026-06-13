from time import sleep
import json

with open("tasks.json", "r+") as fild:
    file = json.load(fild)

tasks = len(file["Tasks"])

def add_task():
    added = {}
    title = input("Please enter the title of the task :  ")
    des = input("Please enter the description :  ")
    while True:
        abelity = input("Please enter abelity [P/D] : ").lower()
        if abelity != "p" and abelity != "d":
            print("Please enter p (pending) or d (done) .")
        else:
            break
    added["id"] = tasks + 1
    added["Title"] = title
    added["description"] = des
    added["status"] = "Done" if abelity == "d" else "Pending"
    file["Tasks"].append(added)
    print("The task has been added succes !")
def View_Tasks():
    files = json.dumps(file["Tasks"], indent=2)
    print(files)
def Save_Tasks():
    with open("tasks.json", "w") as closes:
        json.dump(file, closes, indent=2)
    print("The file has been saved .")
def Delete_Task():
    try:
        id_number = int(input("Please enter the ID number :  "))
        del file["Tasks"][id_number - 1]
    except ValueError:
        print("Please enter a number .")
    except IndexError:
        print("The ID number not found .")
    else:
        print("Task deleted succesfully ....")
        with open("tasks.json", "w") as closes:
            json.dump(file, closes, indent=2)


def Update_Task():
    try:
        id_number = int(input("Please enter the ID number :  "))
        while True:
            abelity = input("Please enter abelity [P/D] : ").lower()
            if abelity != "p" and abelity != "d":
                print("Please enter p (pending) or d (done) .")
            else:
                break
        file["Tasks"][id_number - 1]["status"] = "Done" if abelity == "d" else "Pending"
    except ValueError:
        print("Please enter a number .")
    except IndexError:
        print("The ID number not found .")
    else:
        print("Task Updated succesfully ....")
        with open("tasks.json", "w") as closes:
            json.dump(file, closes, indent=2)


def exit():
    print("Exiting the program ....")
    sleep(2)