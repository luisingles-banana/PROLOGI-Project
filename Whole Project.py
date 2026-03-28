def deadline_tracker():
    tasks = []
    due_date = []
    days_remaining = []

    print("Enter today's date")

    # Has no validation of number of days
    today_year = int(input("Year: ")) #INT
    today_month = int(input("Month (1-12): ")) #INT
    today_day = int(input("Day (1-31): ")) #INT

    while True:
        print(f"\nDate Today: {today_month}/{today_day}/{today_year}")
        print("===== TASK LIST =====")
        header = ("ID", "Task", "Due Date", "Days Remaining")
        print(f"{header[0]:<5}{header[1]:<15}{header[2]:<15}{header[3]:<20}")

        for i in range(len(tasks)):
            print(f"{i:<5}{tasks[i]:<15}{due_date[i]:<15}{days_remaining[i]:<20}")

        option = input("\nEnter 1 to Add Deadlines, 2 to Remove Tasks, 0 to Exit: ")
        match option:
            case "1":
                task = input("Enter task: ") #STRING
                tasks.append(task)

                # Has no validation of number of days
                print("\nDue Date")
                due_year = int(input("Year: ")) #INT
                due_month = int(input("Month (1-12): ")) #INT
                due_day = int(input("Day (1-31): ")) #INT

                due_date.append(f"{due_month}/{due_day}/{due_year}")

                add_day == 0
                if (month % 2) == 0:
                    add_day = month // 2
                    
                today_total = today_year * 365 + today_month * 30 + today_day + add_day
                due_total = due_year * 365 + due_month * 30 + due_day + add_day
                days = due_total - today_total
                days_remaining.append(f"{days} Days Remaining")

            case "2":
                if len(tasks) == 0:
                    print("No tasks to remove.")
                    continue

                while True:
                    i = input("Enter ID to remove: ")

                    if i.isdigit():
                        i = int(i)

                        if 0 <= i < len(tasks):
                            del tasks[i]
                            del due_date[i]
                            del days_remaining[i]
                            print("Task removed.")
                            break

                    print("Invalid input!")

            case "0":
                print("Exiting Program...!")
                break

            case _:
                print("Invalid choice!")

def flashcard():
    def enumeration():

        # Input Number of Questions
        maxQA = int(input("Number of Questions to be inputted: "))

        # Input the Question and Answers
        questions = [] 
        answers = []
        for i in range(maxQA):
            questions.append(input("\nState the Definition: "))
            answers.append(input("State the Answer: "))

        # Flashcard Game
        while True:
            score = 0
            for i in range(maxQA):
                print("\n" + questions[i])
                answer = input("Answer: ")
                if answer == answers[i]:
                    score += 1
        
            print("Score:", str(score) + "/" + str(maxQA))
            restart = input("Try Again? (Y/N) ")
            if restart.upper() == "N":
                break

    def multipleChoice():

        # Input Number of Questions
        maxQA = int(input("Number of Questions to be inputted: "))

        # Input the Question and Answers
        questions = [] 
        A = []
        B = []
        C = []
        D = []
        answers = []
        for i in range(maxQA):
            questions.append(input("\nState the Definition: "))
            A.append(input("A: "))
            B.append(input("B: "))
            C.append(input("C: "))
            D.append(input("D: "))
        
            while True:
                correctAnswer = input("State the Answer: ")
                if correctAnswer == "A" or correctAnswer == "B" or correctAnswer == "C" or correctAnswer == "D":
                    answers.append(correctAnswer)
                    break
                else: 
                    print("Invalid Answer!")

        # Flashcard Game
        while True:
            score = 0
            for i in range(maxQA):
                print("\n" + questions[i])
                print("A.", A[i])
                print("B.", B[i])
                print("C.", C[i])
                print("D.", D[i])
            
                answer = input("Answer: ").upper()
                if answer == answers[i]:
                    score += 1
        
            print("Score:", str(score) + "/" + str(maxQA))
            restart = input("Try Again? (Y/N) ")
            if restart.upper() == "N":
                break

    # Main code
    while True:
        print("1. Enumeration")
        print("2. Multiple Choice")
        print("3. Exit")
        option = int(input("\nSelect an Option (1,2,3): "))

        match option:   # swtich case
            case 1:
                enumeration()
                break
            case 2:
                multipleChoice()
                break
            case 3:
                break
            case _:     # default
                print("Invalid Option!\n")



# MAIN CODE
while True:
    option = input("""
    0 - Exit
    1 - Flashcard
    2 - Deadline Tracker
        """)

    match option:
        case "1":
            flashcard()
            #continue

        case "2":
            deadline_tracker()
            #continue

        case "0":
            print("Exiting Program...")
            break

        case _:
            print("Invalid Input!")
