import gspread
from google.oauth2.service_account import Credentials
# imported textwrap to improve visuals
import textwrap
# imported datetime to help with date storage
import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("weekly_creche_food_budget")

budget = SHEET.worksheet("budget")

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

        validate_date(year, month, day)
        
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


def calculate_dinner_budget(days):
    """
    Gets the attendance of children over the week and returns the budget allocation
    """
    attendance = int(input(f"Enter number of children attending on {days}:"))
    BUDGET_PER_CHILD = 0.5

    budget = attendance * BUDGET_PER_CHILD
    return budget

def budget_subcatagories(category, total_budget):
    """
    calculates the subcatagories of the total budget
    """
    if (category == "meat"):
        sub_bud = (total_budget / 40) * 100
        return sub_bud
    elif (category == veg):    
        veg = (total_budget / 41) * 100

def main():  
    """
    Run all program functions
    """             
    welcome_message()
    date = get_week_starting()
    monday = calculate_dinner_budget("Monday")
    tuesday = calculate_dinner_budget("Tuesday")
    wednesday = calculate_dinner_budget("Wednesday")
    thursday = calculate_dinner_budget("Thursday")
    friday = calculate_dinner_budget("Friday")
    budget_for_week = monday + tuesday + wednesday + thursday + friday
    meat_sub = budget_subcatagories("meat", budget_for_week)
    veg_sub = budget_subcatagories("veg", budget_for_week)
    herbs_sub = budget_subcatagories("herbs", budget_for_week)
    dairy_sub = budget_subcatagories("dairy", budget_for_week)
    

main() 