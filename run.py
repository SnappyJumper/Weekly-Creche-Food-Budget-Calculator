import gspread
from google.oauth2.service_account import Credentials
# imported textwrap to improve visuals
import textwrap

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
                        
welcome_message()