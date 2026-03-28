def check_date(prompt, min_value, max_value, month=0, year=0):
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Checks if theres 
    if month and year:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if month == 2 and is_leap:
            max_value = 29
        else:
            max_value = days_per_month[month-1]

    while True:
        value = input(prompt).strip()

        if value == "":
            return ""

        if not value.isdigit():
            print("Invalid input!")
            continue

        if not (min_value <= int(value) <= max_value):
            print("Invalid input!")
            continue

        return int(value)

def print_table(tasks, start_date, due_date, days_remaining, today_year, today_month, today_day):
    print(f"\n\nDate Today: {today_month}/{today_day}/{today_year}")
    
    header = ("ID", "Task", "Start Date", "Due Date", "Days Remaining")
    print("\n======================================= Deadline Tracker =======================================")
    print(f"{header[0]:<5}{header[1]:<40}{header[2]:<15}{header[3]:<15}{header[4]:<40}")

    if len(tasks) == 0:
        print("No Tasks.")
    else:
        for x in range(len(tasks)):
            if not(due_date[x] == "No Date"):
                display_rem_days = f"{days_remaining[x]} Days Remaining"
                print(f"{x:<5}{tasks[x]:<40}{start_date[x]:<15}{due_date[x]:<15}{display_rem_days:<40}")
            else:
                print(f"{x:<5}{tasks[x]:<40}{start_date[x]:<15}{due_date[x]:<15}{days_remaining[x]:<40}")

    print("\n-------------------------------------------------------------------------------------------------")

def add_task(tasks, start_date, due_date, days_remaining, today_month, today_year, today_day):
    inp_task = input("Input Task: ")
    tasks.append(inp_task)
    
    print("\nStart Date")
    start_year = check_date("Year (YYYY): ",  1, 9999)
    start_month = check_date("Month (MM): ",   1, 12)
    start_day = check_date("Day (DD): ",     1, 31, month=start_month, year=start_year)
    
    
    print("\nDue Date")
    due_year = check_date("Year (YYYY): ",  1, 9999)
    due_month = check_date("Month (MM): ",   1, 12)
    due_day = check_date("Day (DD): ",     1, 31, month=due_month, year=due_year)
    
    if start_year == "" and start_month == "" and start_day == "":
        start_date.append("No Date")
    else: 
        start_date.append(f"{start_month}/{start_day}/{start_year}")

    if due_year == "" and due_month == "" and due_day == "":
        due_date.append("No Date")
    else: 
        due_date.append(f"{due_month}/{due_day}/{due_year}")

    # Checks how many days remains
    if due_year == "" or due_month == "" or due_day == "":
        days_remaining.append("No Date")
    else: 
        days_remaining.append(compute_days_rem(today_month, today_year, today_day, due_day, due_month, due_year))


def compute_days_rem(today_month, today_year, today_day, due_day, due_month, due_year):
    # If any part of the due date is missing, we can't calculate
    if due_day == "" or due_month == "" or due_year == "":
        return ""

    days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Calculate Today Days
    y1 = today_year - 1
    # Takes the number of days starting from Jan 1, 1 to last year of today
    abs_today = y1 * 365 + (y1 // 4) - (y1 // 100) + (y1 // 400)
    
    # Days from months in current year
    for m in range(1, today_month):
        abs_today += days_in_months[m]
        if m == 2 and ((today_year % 4 == 0 and today_year % 100 != 0) or (today_year % 400 == 0)):
            abs_today += 1
    abs_today += today_day

    # Calculate Due Date Days
    y2 = due_year - 1
    # Takes the number of days starting from Jan 1, 1 to last year of due date
    abs_due = y2 * 365 + (y2 // 4) - (y2 // 100) + (y2 // 400)

    # Days from months in current year
    for m in range(1, due_month):
        abs_due += days_in_months[m]
        if m == 2 and ((due_year % 4 == 0 and due_year % 100 != 0) or (due_year % 400 == 0)):
            abs_due += 1
    abs_due += due_day

    return abs_due - abs_today


def remove_task(tasks, start_date, due_date, days_remaining):
    if len(tasks) == 0:
        print("No tasks to remove.")
        return

    while True:
        remove_id = input("Enter task ID to remove: ")

        if remove_id.isdigit():
            remove_id = int(remove_id)

            if 0 <= remove_id < len(tasks):
                del tasks[remove_id]
                del start_date[remove_id]
                del due_date[remove_id]
                del days_remaining[remove_id]
                print("Task removed.")
                break
            else:
                print("ID out of range.")
        else:
            print("Invalid input!")


# ----------------------------------------------------------------------------------------------------------------------
#
# Main Program
#
# ----------------------------------------------------------------------------------------------------------------------
tasks = []
start_date = []
due_date = []
days_remaining = []

# Input the Date Today
while True:
    print("Enter the Date Today:")
    today_year  = check_date("Year (YYYY): ",  1, 9999)
    today_month = check_date("Month (MM): ",   1, 12)
    today_day   = check_date("Day (DD): ",     1, 31, month=today_month, year=today_year)

    if today_year == "" or today_month == "" or today_day == "":
        print("Invalid Input!\n")
        continue
    break

# Actual Main Program
while True:
    print_table(tasks, start_date, due_date, days_remaining, today_year, today_month, today_day)

    option = input("\nEnter '0' to exit, '1' to add tasks, '2' to remove tasks: ")
    match option:
        case "1":
            add_task(tasks, start_date, due_date, days_remaining, today_month, today_year, today_day)

        case "2":
            remove_task(tasks, start_date, due_date, days_remaining)

        case "0":
            print("Exiting program...")
            break

        case _:
            print("Invalid input.")
