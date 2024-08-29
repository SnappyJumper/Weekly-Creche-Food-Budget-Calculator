# imported textwrap to improve visuals
import textwrap
# imported datetime to help with date storage
import datetime
# imported prettytable to display outputs on a table
from prettytable import PrettyTable
# imported colorama to add some color to terminal
from colorama import Fore, Back, Style


def welcome_message():
    """
    Displays the welcome message
    """
    print()
    print(Fore.BLUE + "Welcome to your creche food budget calculator!\n")
    print(textwrap.fill(Style.RESET_ALL + "Use this handy calculator to"
                        " determine how much your weekly food spend is!"))
    print()
    print(textwrap.fill("The calculator will need the date at the start of the"
                        " week, the capacity of your creche and your daily"
                        " predicted attendance. Using these inputs the"
                        " calculator will give you two tables displaying both"
                        " your inputs and the output budget. The output budget"
                        " will be displayed in full and broken down into"
                        " various subcategories"))


def get_week_starting():
    """
    Gets the current date from the user and stores it to a variable
    """
    print()
    print(Fore.BLUE + "Let's get you started!\n")
    while True:
        print(Style.RESET_ALL + "Please enter the starting date for the week")
        print()
        print("Enter the year:(YYYY) ")
        year = input()
        print()

        print("Enter the month:(MM) ")
        month = input()
        print()

        print("Enter the day:(DD) ")
        day = input()

        if validate_date(year, month, day):
            print()
            print(Fore.GREEN + "Date is valid!")
            print(Style.RESET_ALL)
            date_entered = datetime.date(int(year), int(month), int(day))
            break

    return date_entered


def validate_date(y, m, d):
    """
    Validates the date and returns true if valid or false if not
    """
    try:
        datetime.date(int(y), int(m), int(d))

        if len(y) < 4:
            raise ValueError

    except ValueError:
        print()
        print(Fore.RED + "Date is invalid please enter as YYYY MM DD")
        print(Style.RESET_ALL)
        return False

    return True


def get_creche_capacity():
    """
    Gets the max capacity of the creche from the user
    """
    while True:
        print("Please input the Maximum capacity of your creche:")
        capacity = input()

        if validate_capacity(capacity):
            print()
            print(Fore.GREEN + "Input accepted!")
            print(Style.RESET_ALL)
            capacity = int(capacity)
            break
    return capacity


def validate_capacity(cap):
    """
    Validates the capacity input, ensuring it is a number variable
    and is not under 1.
    """
    try:
        cap = int(cap)

        if cap < 1:
            raise ValueError

    except ValueError:
        print()
        print(Fore.RED + "Invalid input, positive numbers only,"
              " please try again.")
        print(Style.RESET_ALL)
        return False

    return True


def calculate_daily_budget(days, creche_cap):
    """
    Gets the attendance of children on each weekday and
    returns the budget for that day
    """
    while True:
        print(f"Enter number of children attending on {days}: ")

        attendance = input()

        if validate_attendance(attendance, creche_cap):
            print()
            print(Fore.GREEN + "Input accepted!")
            print(Style.RESET_ALL)
            attendance = int(attendance)
            # Budget is fixed variable determined by creche
            BUDGET_PER_CHILD = 0.9
            daily_budget = attendance * BUDGET_PER_CHILD
            break

    result = [attendance, daily_budget]

    return result


def validate_attendance(att, creche_capacity):
    """
    Validates the attendance, ensuring it is over 0 and does not
    exceed the creche capacity.
    """
    try:
        att = int(att)

        if att > creche_capacity:
            raise ValueError
        elif att < 0:
            raise ValueError

    except ValueError:
        print()
        print(Fore.RED + "Input error, input should be a positive number"
              " that does not exceed the creche capacity, please try again")
        print(Style.RESET_ALL)
        return False

    return True


def budget_for_week(mon, tues, weds, thurs, fri):
    """
    Takes the list that was outputted by the calculate dinner budget
    and takes the budget from each list and adds them together
    """
    budget_total = mon[1] + tues[1] + weds[1] + thurs[1] + fri[1]

    return budget_total


def budget_subcategories(category, total_budget):
    """
    calculates the subcatagories of the total budget
    """
    if (category == "meat"):
        # meat budget
        sub_bud = round((total_budget / 100) * 40, 2)
        return sub_bud
    elif (category == "veg"):
        # veg budget
        sub_bud = round((total_budget / 100) * 41, 2)
        return sub_bud
    elif (category == "herbs"):
        # herbs budget
        sub_bud = round((total_budget / 100) * 3, 2)
        return sub_bud
    elif (category == "dairy"):
        # dairy budget
        sub_bud = round((total_budget / 100) * 16, 2)
        return sub_bud


def terminal_table_budget(when, week_budget, meat, veg, herbs, dairy):
    """
    Generates a table to display results on the terminal
    """
    week_budget = round(week_budget, 2)
    # creates a new table and assigns it to a variable
    budget_table = PrettyTable()
    # adds the column names to the table
    budget_table.field_names = ["Week Starting", "Total Budget", "Meat Budget",
                                "Veg Budget", "Herbs Budget", "Dairy Budget"]
    # adds a row to the table
    budget_table.add_row([when, week_budget, meat, veg, herbs, dairy])

    print(Fore.BLUE + "Budget breakdown:\n")
    print(Fore.MAGENTA)
    print(budget_table)
    print(Style.RESET_ALL)


def terminal_table_attendance(week_date, attendance_data, kid_limit):
    """
    Generates another table to display attendance on given days
    """
    # creates a new table and assigns it to a variable
    attendance_table = PrettyTable()

    print()
    print(Fore.BLUE + "Predicted Attendance For The Week:\n")
    # adds the column names to the table
    attendance_table.field_names = ["Week Starting", "Monday", "Tuesday",
                                    "Wednesday", "Thursday", "Friday",
                                    "Creche Daily Capacity"]
    # adds a row to the table
    attendance_table.add_row([week_date, attendance_data[0],
                             attendance_data[1], attendance_data[2],
                             attendance_data[3], attendance_data[4],
                             kid_limit])

    print(Fore.MAGENTA)
    print(attendance_table)
    print(Style.RESET_ALL)


def run_again():
    """
    Allow the user to run the application
    once again or exit
    """
    while True:
        run_again = input(Fore.BLUE +
                          "Would you like to run the calculator again?"
                          + Style.RESET_ALL +
                          "\nTo run again, please enter 'y'."
                          "\nTo exit, please enter 'n'.\n")
        if validate_run_again(run_again):

            if run_again == 'n':
                print(Fore.BLUE + "Thanks for using the Creche Budget"
                      "Calculator, See you soon!")
                print(Style.RESET_ALL)
                print(textwrap.fill(
                                    "If you change your mind and want to"
                                    " run the program again just reset"
                                    " the program or refesh the page"))
                return False
            else:
                return True


def validate_run_again(answer):
    """
    validates the run again input
    """
    try:
        if answer == "y":
            return True
        elif answer == "n":
            return True
        else:
            raise ValueError

    except ValueError:
        print()
        print(Fore.RED + "Input error, answer y or n, please try again")
        print(Style.RESET_ALL)
        return False


def main():
    """
    Run all program functions
    """
    welcome_message()
    while True:
        date = get_week_starting()
        max_kids = get_creche_capacity()
        monday = calculate_daily_budget("Monday", max_kids)
        tuesday = calculate_daily_budget("Tuesday", max_kids)
        wednesday = calculate_daily_budget("Wednesday", max_kids)
        thursday = calculate_daily_budget("Thursday", max_kids)
        friday = calculate_daily_budget("Friday", max_kids)
        final_budget = budget_for_week(monday, tuesday, wednesday,
                                       thursday, friday)
        daily_attendance = [monday[0], tuesday[0], wednesday[0],
                            thursday[0], friday[0]]
        meat_sub = budget_subcategories("meat", final_budget)
        veg_sub = budget_subcategories("veg", final_budget)
        herbs_sub = budget_subcategories("herbs", final_budget)
        dairy_sub = budget_subcategories("dairy", final_budget)
        terminal_table_attendance(date, daily_attendance, max_kids)
        terminal_table_budget(date, final_budget, meat_sub, veg_sub,
                              herbs_sub, dairy_sub)
        run = run_again()
        if not run:
            break


main()
