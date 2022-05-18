from argparse import ArgumentParser
import sys
import re
import random
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter("ignore")

def GraphFilter(dataframe, userinput):
    """Filters through the dataframe that is provided after the game is complete

    Args:
        dataframe (Pandas Dataframe): Contains Funds/Profit data from the store Simulation
        userinput (Str): User input asking which data they would like to display in graph form
    """
    if userinput == "1":
        fundsFiltered = dataframe[dataframe['Type'] == 1]
        graphGenerator(fundsFiltered)
        plt.show()
    elif userinput == "2":
        profitFiltered = dataframe[dataframe['Type']==2]
        graphGenerator(profitFiltered)
        plt.show()
    while input("Would you like to display another graph? (Y/N)").upper() != "N":
        GraphFilter(dataframe, input("Which graphs would you like to display?\n 1: Funds during the game\n 2: Profit During the game\n"))
    print("Thank you for playing")  

def graphGenerator(dataframe):
    dataframe = dataframe[['Day', 'Counter']]
    dataframe.plot()
    plt.show()

    

class Employees():
    '''Creates the Employee class. 
    Attributes:
        employee_ids (list): a list of employee ids
        salary (dict): a dictionary of key values as employee ids and salaries
        schedule (dict): a dictionary of lists where the key values are
        the ids in employee_ids and values are lists representing days on work
    '''
    def __init__(self, num_employees, days, filename):
        """Initializes an Employees object

        Args:
            num_employees (int): the number of initial employers hired
            filename (str, optional): a string containing the path to a file. 
            Defaults to ["Simon"].
        """
        
        employee_ids = dict()
        salary_dict = dict()
        schedule_dict = dict()
        happiness = dict()
        
        employee_names = list()
        with open(filename, "r", encoding = "utf-8") as f:
            curr_count = 0
            for name in f:
                name = name[:-2]
                if curr_count < num_employees:
                    employee_names.append(name)
                    curr_count += 1
                else:
                    break
        for i in range(len(employee_names)):
            employee_ids[i] = employee_names[i]
            salary_dict[employee_names[i]] = random.randint(1, 10)
            happiness[employee_names[i]] = random.randint(70, 100)
            schedule_list = list()
            for j in range(days):
                schedule_list.append(random.randint(0, 1))
            schedule_dict[employee_names[i]] = schedule_list
            
        self.employeenames = employee_names
        self.employee_ids = employee_ids
        self.salaries = salary_dict
        self.schedules = schedule_dict
        self.happiness = happiness
        
    def manageEmploys(self, budgetAmount = 0, val = 0):
        if val == 0:
            payment = 0
            for name in self.salaries:
                payment += self.salaries[name]
            return budgetAmount - payment
        if val == 1:
            while(input("Would you like to keep changing salaries? Y for yes") == "Y"):
                print(self.salaries)
                emp_name = input("Which employee do you want to change the salary of? Type in a name.")
                self.salaries[emp_name] = int(input("What is their new salary?"))
        if val == 2:
            print(budgetAmount)
            newemp = input("What is this new employee's name?")
            self.employeenames.append(newemp)
            self.employee_ids[len(self.employeenames) - 1] = newemp
            newsal = random.randint(1, 10)
            self.salaries[newemp] = newsal
            budgetAmount = budgetAmount - newsal
            newschedule = list()
            for i in range(15):
                newschedule.append(random.randint(0, 1))
            self.schedules[newemp] = newschedule
            self.happiness[newemp] = random.randint(70, 100)
            print(budgetAmount)
            return budgetAmount



def read_stock(filename):
    ''' reads a file that sets the items, prices, and stock.
    opens the file using a with statement and reads with regex.
    Args:
        filename(str): a string containing the directory of the file
        containing the store stock.
    Side effects:
        creates inventory(dict), with keys being tuples of the
        item name and price, and values being the stock amount.
    '''
    with open(filename, "r", encoding = "utf-8") as f:
        inventory = {}
        for line in f:
            expr = (r"""(?mx)
                    ^
                    (?:(?P<item>[a-z]+)*\s)
                    (?P<price>\d*)""")
            match = re.search(expr,line)
            if match:
                itemname = match.group("item")
                itemprice = match.group("price")
                itemlisting = (itemname, itemprice)
                inventory[itemlisting] = 50    
    return inventory        
    
def run_game(EmployeeFilePath, StockFilePath):
        dfmainTracker = pd.DataFrame(columns = ['Type','Day', 'Counter'])
        profit = 0
        dayCounter = 1
        fundsCounter = 1000
        dfmainTracker = dfmainTracker.append({'Type':1, 'Day':dayCounter, 'Counter':fundsCounter}, ignore_index=True)
        dfmainTracker = dfmainTracker.append({'Type':2, 'Day':dayCounter, 'Counter':profit}, ignore_index=True)
       #simlation runs for 5 days. 
        max_days = 5
        employee = Employees(int(input("How many employees do you want?")), max_days, EmployeeFilePath)
        """Runs a full simulation game, over a series of 
            game days.
                
            Side effects: Prints the game result to the terminal. 
        """
        
        
        
        #populate inventory with the available stock
        inventory = read_stock(StockFilePath)
        
        #continues looping and running the simulation until the player 
        #completes 5 days or runs out of money
        while dayCounter < max_days + 1 and fundsCounter > 0:
            dayCounter, fundsCounter, profit, inventory = run_day(dayCounter, fundsCounter, profit, inventory, employee)
            dfmainTracker = dfmainTracker.append({'Type':1, 'Day':dayCounter, 'Counter':fundsCounter}, ignore_index=True)
            dfmainTracker = dfmainTracker.append({'Type':2, 'Day':dayCounter, 'Counter':profit}, ignore_index=True)

        #player loses if they run out of money
        if fundsCounter <= 0:
             print(f'''Sorry, you ran out of money after day {dayCounter - 1}''')
             
        #return either a win message or a lose message after 5 days. 
        #win condition is currently $500 dollars profit
        if profit >= 500:
            print(f'''Congratulations, you won the game. You made
                  ${profit} in 5 days''')
        else:
            print(f'''Sorry, you lost the game. You only made 
                  ${profit} in 5 days.''')
        return dfmainTracker
        
        
def run_day(day, funds, profit, inventory, employeeObj):
        """Prints store status, calls the store simulation method, then
        increases the day.
        
        Side effects: 
            Prints information to the terminal for the player to 
            see store status
            Can modifiy the day variable.
        """
        #give player store status
        print(f'''Welcome to day {day}. Here is the status of your 
              store:''')
        
        #print finances
        print(f'''Your profit so far is ${profit}''')
        print(f'''Your current funds are ${funds}''')
        #print inventory
        print('''Here is an overview of your current store inventory:''')
        
        #print each item 
        itemindex = 0
        itemslist = list(inventory)
        while itemindex < 15:
            item = itemslist[itemindex]
            print(f'Item: {item[0]}, Price: ${item[1]}, Quantity: {inventory[itemslist[itemindex]]}')
            itemindex += 1

        #simulation will now run
        print(f'''The simulation for day {day} will now run''')
                
        #run a simulation of customers buying items in the store for a day
        inventory, sim_profit = simulate_day(inventory,profit, employeeObj)
        while(input("Would you like to manage employees?") == "Y"):
            print("What action do you want to do?")
            print("0 <- Pay salaries")
            print("1 <- Adjust salaries")
            print("2 <- Add employee")
            choice = int(input())
            if choice == 0:
                print(funds)
                funds = employeeObj.manageEmploys(funds)
                print("Current funds: ", funds)
            if choice == 1:
                employeeObj.manageEmploys(val = 1)
            if choice == 2:
                funds = employeeObj.manageEmploys(budgetAmount = funds, val = 2)
        profit += sim_profit
        funds += profit
        
        #increase the day variable
        day += 1
        return day, funds, profit, inventory

def simulate_day(inventory,profit, employeeObj):
    '''Runs the customer purchasing simulation activities for one 
    game day. The purchasing simulation is mainly random but may be 
    influenced by certain external events in the game.
                
    Args: 
        inventory(dict): the inventory of the store
        profit(int): the current profit of the player
        employeeObj(employee): the employee data for the store
        
    Returns: 
        inventory(dict): the inventory of the store
        profit(int): the profit of the player
    
    Side Effects:
        Can modify the profit and inventory. 
        prints information to the console.
    '''
    maxcustomers = len(employeeObj.employee_ids) * 15
    customercount = random.randint(0,maxcustomers)
    print(f"{customercount} customer(s) came to the store today.")
    itemslist = list(inventory)
    for person in range(customercount):
        itemindex = random.randint(0, 14)
        purchase = itemslist[itemindex]
        price = purchase[1]
        if inventory.get(purchase) == 0:
            continue
        currentamount = inventory.get(purchase)
        inventory[itemindex] = currentamount
        newamount = inventory[itemslist[itemindex]] = currentamount - 1
        profit += int(price)
        print(f"""customer {person + 1} bought 1 {purchase[0]} for ${price}. \
                the previous amount was {currentamount}. the new amount is {newamount}. \
                profit is now ${profit}.""")
    return inventory, profit
    
def main(EmployeeFilePath, StockFilePath):
    GraphFilter(run_game(EmployeeFilePath, StockFilePath), input("Which graphs would you like to display?\n 1: Funds during the game\n 2: Profit During the game\n"))
    
    
def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("EmployeeList", help = "Excel file of employees")
    parser.add_argument("StockList", help = "The text file of the stock for the store")
    return parser.parse_args(arglist)    

if __name__ == "__main__":
    args  = parse_args(sys.argv[1:])
    main(args.EmployeeList, args.StockList)