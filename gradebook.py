try:
    while True:
        print("***-Grade Book menu-***")
        print("1. Add students and score")
        print("2. View all students and average score")
        print("3. Exit")
        user_choice = input("Enter your choice: ")
        if user_choice == "1":
            print("You chose to add a student")
        elif user_choice == "2":
            print("You chose to view all students")
        elif user_choice == "3":
            break
except Exception as eror:
    print(f"eror : {eror}")