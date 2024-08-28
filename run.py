# imported textwrap to improve visuals
import textwrap
# imported datetime to help with date storage
import datetime
# imported prettytable to display outputs on a table
from prettytable import PrettyTable

def welcome_message():
    """
    Displays the welcome message
    """
   
    print("Welcome to your creche food budget calculator!\n")
    print(textwrap.fill("Use this handy calculator to determine how" 
                        " much your weekly food spend on vegetables and meat should be."))
    print()
    print(textwrap.fill("The calculator will take inputs of the predicted attendance of" 
                        " children and staff for the coming week and ask if there are" 
                        " any vegetarians present. Then it will output your individual" 
                        " budgets for Meat and Vegetables to a spreadsheet."))

def get_week_starting():
    """
    Gets the current date from the user and stores it to a variable
    """
    print("Let's get you started!\n")
    while True:
        print("Please enter the starting date for the week")
        print("Enter the year: ")
        year = input()

        print("Enter the month: ")
        month = input()

        print("Enter the day: ")
        day = input()
        
        if validate_date(year, month, day):
            print("Date is valid!")
            date_entered = datetime.date(int(year), int(month), int(day))
            break      
            
    return date_entered

def validate_date(y, m, d):
    """
    Validates the date and returns true if valid or false if not
    """
    try:
        datetime.date(int(y), int(m), int(d))
    
    except ValueError:
        print("Date is invalid please enter as YYYY MM DD")
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
            print("Input accepted!") 
            capacity = int(capacity)
            break
    return capacity
    
def validate_capacity(cap):
    """
    Validates the capacity input
    """
    try:
        cap = int(cap)
        
        if cap < 1 :
            raise ValueError
        
    except ValueError:
        print("Invalid input, please try again.")
        return False
    
    return True

def calculate_daily_budget(days, creche_cap):
    """
    Gets the attendance of children over the week and returns the
    budget allocation
    """
    while True:
        attendance = input(f"Enter number of children attending on {days}: ")
        
        if validate_attendance(attendance, creche_cap):
            print("input accepted!")
            attendance = int(attendance)
            BUDGET_PER_CHILD = 0.3
            daily_budget = attendance * BUDGET_PER_CHILD
            break
    
    result = [attendance, daily_budget]

    return result

def validate_attendance(att, creche_capacity):
    try:
        att = int(att)

        if att > creche_capacity:
            raise ValueError
        elif att < 0:
            raise ValueError


    except ValueError:
        print("Input error, please try again")
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
        sub_bud = round((total_budget / 100) * 40, 2)
        return sub_bud
    elif (category == "veg"):    
        sub_bud = round((total_budget / 100) * 41, 2)
        return sub_bud
    elif (category == "herbs"):
        sub_bud = round((total_budget / 100) * 3, 2)
        return sub_bud
    elif (category == "dairy"):
        sub_bud = round((total_budget / 100) * 16, 2)
        return sub_bud

def terminal_table_budget(when, week_budget, meat, veg, herbs, dairy):
    """
    Generates a table to display results on the terminal
    """
    budget_table = PrettyTable()

    budget_table.field_names = ["Week Starting", "Total Budget", "Meat Budget",
     "Veg Budget", "Herbs Budget", "Dairy Budget"]
    budget_table.add_row([when, week_budget, meat, veg, herbs, dairy])

    print(budget_table)

def terminal_table_attendance(week_date, attendance_data):
    """
    Generates another table to display attendance on given days
    """
    attendance_table = PrettyTable()

    print("Predicted Attendance For The Week:")

    attendance_table.field_names = ["Week Starting", "Monday", "Tuesday",
     "Wednesday", "Thursday", "Friday"]
    attendance_table.add_row([week_date, attendance_data[0], attendance_data[1],
     attendance_data[2], attendance_data[3], attendance_data[4]])

    print(attendance_table)

def run_again():
    '''
    Allow the user to run the application
    once again or exit
    '''
    while True:
        run_again = input(
                        "Would you like to run the calculator again?"
                        "\nTo run again, please enter 'y'."
                        "\nTo exit, please enter 'n'.\n")
        if validate_run_again(run_again):

            if run_again == 'n':
                print("Thanks for using the Creche Budget Calculator, See you soon!")
                print(textwrap.fill(
                                    "If you change your mind and want to run the program again"
                                    " just reset the program or refesh the page"))
                return False
            else:
                return True

def validate_run_again(answer):
    try:
        if answer == "y":
            return True
        elif answer == "n":
            return True
        else:
            raise ValueError
    
    except ValueError:
        print("Input error, please try again")
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
        final_budget = budget_for_week(monday, tuesday, wednesday, thursday, friday)
        daily_attendance = [monday[0], tuesday[0], wednesday[0], thursday[0], friday[0]]
        meat_sub = budget_subcategories("meat", final_budget)
        veg_sub = budget_subcategories("veg", final_budget)
        herbs_sub = budget_subcategories("herbs", final_budget)
        dairy_sub = budget_subcategories("dairy", final_budget)
        terminal_table_budget(date, final_budget, meat_sub, veg_sub, herbs_sub, dairy_sub)
        terminal_table_attendance(date, daily_attendance)
        run = run_again()
        if not run:
            break
    
main() 