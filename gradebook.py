try:
    students = dict()
    while True:
        print("***-Grade Book menu-***")
        print("1. Add students and score")
        print("2. View all students and average score")
        print("3. Exit")
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            print("**-Add student-**")
            std_name = input("Enter student name: ").strip()
            std_scores = input("Enter student score: ").split()
            std_scores = [float(score) for score in std_scores]
            students[std_name] = std_scores
            std_scores = []
            print(students)
        elif user_choice == "2":
            print("You chose to view all students")
        elif user_choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice")
except Exception as eror:
    print(f"eror : {eror}")