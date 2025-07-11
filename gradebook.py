import json
import  os
try:
    students = dict()
    if os.path.exists('students.json'):
        with open('students.json', "r") as file:
            students = json.load(file)
    else:
        students = {}
    std_averages = dict()
    while True:
        print("***-Grade Book menu-***")
        print("1. Add students and score")
        print("2. View all students and average score")
        print("3. Delete student")
        print("4. Exit")
        user_choice = input("Enter your choice: ")
        print("-" * 20)
        if user_choice == "1":
            print("**-Add student-**")
            std_name = input("Enter student name: ").strip()
            std_scores = input("Enter student score: ").split()
            std_scores = [float(score) for score in std_scores]
            students[std_name] = std_scores
            std_scores = []
            with open("students.json", "w") as file:
                json.dump(students, file)
            print(f"student {std_name} successfully added")
            print("-" * 20)
        elif user_choice == "2":
            print("**-View students-**")
            if students:
                for std_name, std_scores in students.items():
                    avg_score = sum(std_scores) / len(std_scores)
                    std_averages[std_name] = round(avg_score, 2)
                for std_name, std_average in std_averages.items():
                    print(f"{std_name} average score: {std_average}")
            else:
                print("No students added")
            print("-" * 20)
        elif user_choice == "3":
            print("**-Delete student-**")
            del_name = input("Enter student name to delete: ").strip()
            if del_name in students:
                del students[del_name]
                del std_averages[del_name]
                with open("students.json", "w") as file:
                    json.dump(students, file)
                print(f"student {del_name} successfully deleted")
                print("-" * 20)
            else:
                print("Student not found")
                print("-" * 20)
        elif user_choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")
except Exception as eror:
    print(f"eror : {eror}")