# Creche Budget Calculator

The Creche Budget Calculator is designed to help the users to organise the weekly food budget for their creche.

It can calculate the total budget for the creche per week and also allocate that budget to a few subcategories like meat, veg and dairy.

Visit the deployed application [here]().

## Table of Contents
1. [User Experience (UX)](#user-experience-UX)
    1. [Project Goals](#project-goals)
    2. [User Stories](#user-stories)
    3. [Color Scheme](#color-scheme)
    4. [Data Model](#data-model)
    5. [Flowchart](#flowchart)
2. [Features](#features)
    1. [Date Entry](#date-entry)
    2. [Creche Capacity Entry](#creche-capacity-entry)
    3. [Predicted Attendance Entry](#predicted-attendance-entry)
    4. [Weekly Budget Calculator](#weekly-budget-calculator)
    5. [Budget Subcategory Calculator](#budget-subcategory-calculator)
    6. [Restart Program](#restart-program)
    7. [Future Features](#future-features)
3. [Technologies Used](#technologies-used)
    1. [Language Used](language-used)
    2. [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
4. [Testing](#testing)
    1. [Testing User Stories](#testing-user-stories)
    2. [Code Validation](#code-validation)
    3. [Manual Testing](#manual-testing)
5. [Deployment](#deployment)
6. [Credits](#credits)
7. [Acknowledgements](#acknowledgements)

***

## User Experience (UX)

### Project Goals

* Have a welcome page that explains the calculator enough that its easy to use even for the first time.

* Every stage in the program is intuitive and the user understands what they need to do next easily.

* Input validation will be present so that the correct data types are entered into the calculator, thus reducing the chance of errors occuring.

* The outputted data should be easy to understand and display clearly.

* The program should continue to run until the user is finished with it.

### User Stories

* As a user, I want to be able to easily understand the purpose and use of the program.

* As a user, I want to be able to easily understand what data and data type I am required to input at each input step.

* As a user, I want to receive feedback about the data I entered so I know it was accepted.

* As a user, I want my inputs to be displayed in an easy to read manner so that I remember what data I entered and check that I did not make any mistakes.

* As a user, I want the output to be displayed in a easy to read manner so there is no confusion what I am looking at.

### Color Scheme

### Data Model

Simple data such as the date and the capacity are stored and returned as variables

More complex variables like attendance and daily budget are stored on variables and returned as lists.

The calculations are stored to variables so that they can be formatted and displayed back to the user.

### Flowchart 

The flowchart was designed using [Miro](https://miro.com/). It was used to help plan the logic implemented in the program.

[Flowchart]

As shown in the flowchart the process has changed and some functionality was added and dropped during development but the main idea demonstrated is the same.

[Back to top ^](#creche-budget-calculator)

## Features

### Date Entry

Collects the date of the Monday of the week and stores it to a variable. This is useful for when the output displays later. If the user runs the program multiple times for different weeks the date will help them differenciate between each output.

### Creche Capacity Entry

Collects the total capacity of the users creche and stores it to a variable. This is then displayed in the output and is also used to limit the predicted attendance input so the user cannot enter a value higher than the capacity they entered.

### Predicted Attendance Entry

Collects the attendance on each weekday 
