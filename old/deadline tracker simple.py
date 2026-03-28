def get_value(prompt):
    while True:
        value = input(prompt)

        if value == "":
            return ""

        if value.isdigit():
            return int(value)

        print("Invalid input!")


def days_remaining_calc(today_year, today_month, today_day, due_year, due_month, due_day):
    # Simple approximation (for easy flowcharting)
    today_total = today_year * 365 + today_month * 30 + today_day
    due_total = due_year * 365 + due_month * 30 + due_day
    return due_total - today_total


def print_table(tasks, due_date, days_remaining):
    print("\n===== TASK LIST =====")
    header = ("ID", "Task", "Due Date", "Days Remaining")
    print(f"{header[0]:<5}{header[1]:<15}{header[2]:<15}{header[3]:<20}")
    if len(tasks) == 0:
        print("No tasks.")
        return

    for i in range(len(tasks)):
        print(f"{i:<5} {tasks[i]:<15} {due_date[i]:<15} {days_remaining[i]:<20}")


def add_task(tasks, due_date, days_remaining, today_year, today_month, today_day):
    task = input("Enter task: ")
    tasks.append(task)

    print("\nDue Date")
    due_year = get_value("Year: ")
    due_month = get_value("Month: ")
    due_day = get_value("Day: ")

    if due_year == "" or due_month == "" or due_day == "":
        due_date.append("No Date")
        days_remaining.append("No Date")
    else:
        due_date.append(f"{due_month}/{due_day}/{due_year}")
        days = days_remaining_calc(today_year, today_month, today_day, due_year, due_month, due_day)
        days_remaining.append(f"{days} Days Remaining")


def remove_task(tasks, due_date, days_remaining):
    if len(tasks) == 0:
        print("No tasks to remove.")
        return

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


# MAIN PROGRAM
tasks = []
due_date = []
days_remaining = []

print("Enter today's date")
today_year = get_value("Year: ")
today_month = get_value("Month: ")
today_day = get_value("Day: ")

while True:
    print_table(tasks, due_date, days_remaining)

    choice = input("\nEnter 1 to Add Deadlines, 2 to Remove Tasks, 0 to Exit: ")

    if choice == "1":
        add_task(tasks, due_date, days_remaining, today_year, today_month, today_day)

    elif choice == "2":
        remove_task(tasks, due_date, days_remaining)

    elif choice == "0":
        print("Exiting Program...!")
        break

    else:
        print("Invalid choice!")