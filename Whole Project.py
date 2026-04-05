def deadline_tracker():
    def check_date(prompt, min_value, max_value):
        while True:
            check_value = int(input(prompt))                                         #INT

            # Checks if less than min_value or more than max_value
            if check_value < min_value or check_value > max_value:
                print("Invalid Input")
                continue
            else:
                break

        return check_value

    tasks = []                                                                       #STRING
    due_date = []                                                                    #STRING
    days_remaining = []                                                              #STRING
    number_of_tasks = 0                                                              #INT

    # Input for Date Today
    print("Enter today's date")
    today_year = check_date("Year: ", 1, 9999)                                       #INT
    today_month = check_date("Month: ", 1, 12)                                       #INT    

    # Checks if Leap Year
    days_per_month_today = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]          #ARRAY 
    if (today_year % 4 == 0 and today_year % 100 != 0) or (today_year % 400 == 0):
        days_per_month_today[1] = 29                                                 #INT

    today_day = check_date("Day: ", 1, days_per_month_today[today_month - 1])        #INT

    while True:
        # Prints Table
        print(f"\n\nDate Today: {today_month}/{today_day}/{today_year}")
        print("===== TASK LIST =====")
        header = ("ID", "Task", "Due Date", "Days Remaining")
        print(f"{header[0]:<5}{header[1]:<15}{header[2]:<15}{header[3]:<20}")

        for i in range(number_of_tasks):
            print(f"{i:<5}{tasks[i]:<15}{due_date[i]:<15}{days_remaining[i]:<20}")

        # Options
        option = input("\nEnter 1 to Add Deadlines, 2 to Remove Tasks, 0 to Exit: ")
        match option:
            case "1":
                task = input("Enter task: ")                                          #STRING
                tasks.append(task)

                # Due Date
                print("\nDue Date")
                due_year = check_date("Year: ", 1, 9999)                              #INT
                due_month = check_date("Month: ", 1, 12)                              #INT    

                # Checks if Leap Year. Changes the 2nd month to 29 days
                days_per_month_due = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #ARRAY 
                if (due_year % 4 == 0 and due_year % 100 != 0) or (due_year % 400 == 0):
                    days_per_month_due[1] = 29                                        #INT

                due_day = check_date("Day: ", 1, days_per_month_due[due_month - 1])   #INT

                due_date.append(f"{due_month}/{due_day}/{due_year}")                  #STRING; idk how to do this in pseudocode

                # Day Calculation
                # Calculates number of days last year of today_year from year 0  
                today_leap_count = today_year // 4 - today_year // 100 + today_year // 400  #INT
                today_total = today_year * 365 + today_leap_count                     #INT
                for m in range(today_month - 1):
                    today_total += days_per_month_today[m]
                today_total += today_day

                # Calculates number of days last year of due_year from year 0
                due_leap_count = due_year // 4 - due_year // 100 + due_year // 400    #INT
                due_total = due_year * 365 + due_leap_count                           #INT
                for m in range(due_month - 1):
                    due_total += days_per_month_due[m]
                due_total += due_day

                # Calculate Number of Days from current day
                days = due_total - today_total

                days_remaining.append(f"{days} Days Remaining")

                number_of_tasks += 1
                continue

            case "2":
                if number_of_tasks == 0:
                    print("Nothing to remove!")
                    continue

                rem = check_date("Enter Task to Remove: ", 0, number_of_tasks - 1)        # INT

                # shift everything left to fill the gap
                i = rem
                while i < number_of_tasks - 1:                                            # for (int i = rem; i < number_of_tasks - 1; i++){
                    tasks[i] = tasks[i + 1]
                    due_date[i] = due_date[i + 1]
                    days_remaining[i] = days_remaining[i + 1]
                    i += 1

                # Removes the last slot of the array (duplicate)
                tasks[number_of_tasks - 1] = ""
                due_date[number_of_tasks - 1] = ""
                days_remaining[number_of_tasks - 1] = ""

                number_of_tasks -= 1
                print("Task Removed!")
                continue

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
