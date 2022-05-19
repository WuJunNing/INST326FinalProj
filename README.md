## Functionality of files in the repository<br>
StoreSim.py is the main program, and will run the store simulation. The store will be managed and simulated using this file.<br>
storestock.txt contains all the items for the store, and their prices. 
- This file will be read by the read_stock function to fill the inventory of the store and prices will be used to calculate the profits.<br>
employeenames.txt contains a list of names of the employees to be read by the program. 
- This will be read by the program to get employees names for the salary dictionary.<br>

## Running the program from the command line<br>
Enter the following into the command line:<br>
`StoreSim.py employeenames.txt storestock.txt`<br>
These files, in order, are the main program, the list of employees, and the store's stock.<br>

## Using the program and interpreting output <br>
For each day simulated, follow the prompts printed to manage the employees and keep your store afloat.<br>
Major outputs:
- Separated by "Press enter to continue sections
- Your Employees: Prints out employee names, salaries, and their happiness guage
- A status message indicating the current day
- Current profit and funds for the given day
- An overview of items, prices, and their inventory
- A simulation of customers, what they bought, inventory amounts, and profit gained along with funds after paying salaries
- Prompts that is used to manage employees.
- Prompts that is used to graph the history of the store
Employee Prompts follow this path for a day:
(1). "How many employees do you want? Max 10" - Number of employees you want to start off with.
- Receives any input integer value from 1 to 10
(2). Multiple series of "Press enter to continue" prompts are asked throughout the outputs
- Receives any input/press enter to continue the next outputs
(3). "Would you like to manage employees? Y/Yes for yes" 
- Receives any input in any capitalization of y and yes as yes and other values as no.

(3.1). "What would you like to do with employees?"
- Asked if you answer yes to prompt (3). Receives any integer value frm 0-5.

(3.1.0). "Would you like to boost an employee? Y/Yes for yes"
- Asked if you picked option 0 in prompt (3.1). 
- Receives any input in any capitalization of y and yes as yes and other values as no.
- Loops back to (3) at a other value response
(3.1.0.y). "Which employee do you want to pay an extra salary? Type in a name."
- Asked if you responded yes to prompt (3.1.0)
- Receives any employee name found within the dictionary printed above. 
- Prints onto the console the old and new boosted salary
- Loops back to (3.1.0)

(3.1.1). "Would you like to change salaries? Y/yes for yes"
- Asked if you picked option 1 in prompt (3.1)
- Receives a yes/y input. 
- Loops back to (3)
(3.1.1.y). "Which employee do you want to change the salary of? Type in a name."
- Asked if yes was the response to prompt (3.1.1)
- Receives any input of a key value in a dictionary printed above
(3.1.1.y.1). "What is their new salary?
- Receives any positive integer input. 
- Loops back to (3.1.1)

(3.1.2). "What is this new employss's name?
- Asked if option 2 was chosen in prompt (3.1)
- Receives any value for an employee name
- Prints out the new employee's salary and funds that are your funds minus the salary
- Prompts a (2) prompt

(3.1.3). "What information would you like?" 
- Asked if option 3 was chosen in prompt (3.1)
- Receives integer values from 1 to 4 for a selection of choices
- input (1): prints out the number of employees working for the day and whether this was over half your employees
- input (2): prints out the average salary of workers, your average profit per employee for the day, and whether the salary is less than profit
- input (3): prints out a happiness level and whether this is above 50 which represents a 50% chance for your employees to be working
- input (4): prints out employee names, their salaries in a dictionary, and the employee happiness level
(3.1.4). 
- Chocie 4 for prompt (3.1) prints out salaries of all employees
(3.1.5).
- Choice 5 for prompt (3.1) skips the managing employees and moves onto the next day

Graphing prompts:
(4). "Which graphs would you like to display?"
- Prompts 2 options for 1. Funds during the game and 2. Profit during the game for graphing
- Output displays a graph indicating a days as x value to profit/funds as y values
(4.1). "Would you like to display another graph? (Y/N)"
- Prompts after prompt (4) if option 3 was not chosen 
- Prompts prompt (4) if a yes option was given

At the end of the simulation, you will either win or lose, depending on how high a profit made.<br>
At the end of the simulation, you will be the option between 2 different graphs to display. One will be funds over time, and the other will be profit over time.<br>

## Attributions
Luis: graphFilter() and graphGenerator() functions. pandas and data visualization.<br>
Simon: Employee class and its methods. optional parameters/keyword arguments(manageEmploys()) and conditional expressions(employInfo()).<br>
Ogenna: run_game() and run_day() functions. f-strings and sequence unpacking.<br>
Yabing: read_stock() and simulate_day() functions. regular expressions and with statements.<br>

## Citations
“Warnings - Warning Control.” Python 3.10.4 Documentation, Python Software Foundation, https://docs.python.org/3/library/warnings.html.<br>
Usage: Program relies on using Pandas.append() Method in order to operate the dataframes used for graphing, this module silences all FutureWarning warnings prompted by the program.
