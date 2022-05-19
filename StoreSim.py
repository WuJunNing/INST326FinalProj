from argparse import ArgumentParser
import sys
import re
import random
import pandas as pd
import matplotlib.pyplot as plt
#------------------------------
# This import for "Warnings" is to mute the warnings that happen throughout
# the program for pandas ".append()". The warnings import is taken from the
# Python doucmentation "warning control". A full citation of this module 
# can be found in the README.
import warnings
warnings.simplefilter("ignore")
#----------------------------------------------------------------

yeses = ["YES", "Y"]
def GraphFilter(dataframe, userinput):
    """Filters through the dataframe provided after the game is complete.
    Generates a graph of the data for the user to see.

    Args:
        dataframe (Pandas Dataframe): Contains Funds/Profit data from the
        store Simulation
        userinput (Str): User input of which choice of graph/data the
        user would like to see.
    Side effects:
        prints prompts to the user to display more graphs if needed.
    
    """
    if userinput == "1":
        fundsFiltered = dataframe[dataframe['Type'] == 1]
        graphGenerator(fundsFiltered)
        plt.show()
        cmd = input("Would you like to display another graph? (Y/Yes)").upper()
        if cmd in yeses:
            GraphFilter(dataframe, input("Which graph would you like to see?"
                                         + "\n 1: Funds during the game"
                                         + "\n2: Profit During the game\n"))
        else:
            pass
    elif userinput == "2":
        profitFiltered = dataframe[dataframe['Type']==2]
        graphGenerator(profitFiltered)
        plt.show()
        cmd = input("Would you like to display another graph? (Y/Yes)").upper()
        if cmd in yeses:
            GraphFilter(dataframe, input("Which graph would you like to see?"
                                         + "\n 1: Funds during the game"
                                         + "\n 2: Profit During the game\n"))
        else:
            pass

def graphGenerator(dataframe):
    """Generates graph based on provided dataframe

    Args:
        dataframe (Pandas Dataframe): Contains Day Number and Counter Nummber
        information based on graph provided by the store simulation program. 
    Side effects:
        creates and shows the graphed data for the user to see.
    """
    dataframe = dataframe[['Day', 'Counter']]
    dataframe.plot()
    plt.show()

    

class Employees():
    '''Creates the Employee class. 
    Attributes:
        employeenames (list): a list strings of employee names
        salaries (dict): a dictionary of random salaries with 
        key valyes in employeenames
        happiness (int): a happiness scale of employees. 
        Fluctuates with decisions
    '''
    def __init__(self, num_employees, filename):
        """Initializes an Employees object

        Args:
            num_employees (int): the number of initial employers hired
            filename (str, optional): a string containing the path to a
            file of employee names 
        """
        
        salary_dict = dict()
        employee_names = list()
        
        #opens a text file of names and fills employee_names with names 
        # in order equal to the number chosen by the player
        with open(filename, "r", encoding = "utf-8") as f:
            curr_count = 0
            for name in f:
                name = name[:-2]
                if curr_count < num_employees:
                    employee_names.append(name)
                    curr_count += 1
                else:
                    break
                
        #Random salaries from 7 to 10 are given to the employees      
        for i in range(len(employee_names)):
            salary_dict[employee_names[i]] = random.randint(7, 10)
            
        #assigned attributes
        self.employeenames = employee_names
        self.salaries = salary_dict
        self.happiness = 100
        
    def manageEmploys(self, val=0, budget=0, profit_earned=0, num_emp=0):
        """Based on various user inputs, manages values of Employee 
        class attributes

        Args:
            val (int, optional): A user input value to run a specific action.
            Defaults to 0.
            budget (int, optional): A budget value indicating how much
            money is left. Defaults to 0.
            profit_earned (int, optional): A profit value of how much profit
            was made. Defaults to 0.
            num_emp (int, optional): A value indicating the number of 
            employees worked. Defaults to 0.

        Returns:
            _type_: _description_
        Side effects:
            prints out messages to the console asking for user input and
            status messages of employee attributes
        """
        #val == 0 multiples a player salary and happiness and subtracts from
        # funds a certain amount equal to the new salaries
        if val == 0:
            total_pay = 0
            while(input("Would you like to boost an employee?" +
                        " Y/Yes for yes \n").upper() in yeses):
                print(self.salaries)
                emp_name = input("Which employee do you want to"
                                 + " pay an extra salary? Type in a name. \n")
                while (emp_name in self.employeenames) == False:
                    print("They are not an employee.")
                    emp_name = input("Please pick an employee name. \n")
                
                print("Current salary: ", self.salaries[emp_name])
                self.salaries[emp_name] *= 2.0
                print("New salary: ", self.salaries[emp_name])
                total_pay += self.salaries[emp_name]
                self.happiness *= 1.1
            return budget - total_pay
        
        #val == 1 loops as long as the player wants to adjust salary
        if val == 1:
            while(input("Would you like to change salaries?"
                        + " Y/yes for yes \n").upper() in yeses):
                print(self.salaries)
                emp_name = input("Which employee do you want to "
                                 + "change the salary of? Type in a name. \n")
                while (emp_name in self.employeenames) == False:
                    print("They are not an employee.")
                    emp_name = input("Please pick an employee name. \n")
                curr_sal = self.salaries[emp_name]
                new_sal = -1
                try:
                    new_sal = int(input("What is their new salary? \n"))
                except:
                    ValueError
                while isinstance(new_sal, int) == False or new_sal < 0:
                    print("That is not a valid salary.")
                    try:
                        new_sal = int(input("What is their new salary? \n"))
                    except:
                        ValueError
                self.salaries[emp_name] = new_sal
                if curr_sal > new_sal:
                    self.happiness /= 1.5
                    print("Your employees did not like this.")
        #val == 2 adds a new employee
        if val == 2:
            print("Total funds: ", budget)
            newemp = input("What is this new employee's name? \n")
            self.employeenames.append(newemp)
            newsal = random.randint(1, 10)
            self.salaries[newemp] = newsal
            budget = budget - newsal
           
            print("This new employee has a salary of", self.salaries[newemp])
            print("Your leftover funds is: ", budget)
            print(input("Press enter to continue"))
            return budget
        #val == 3 provides a selection of options where the player can get 
        # different information on the employees
        if val == 3:
            print("What information would you like?")
            print("1 <- Number of working employees")
            print("2 <- Average salary and whether you pay"
                  + " more than you profit")
            print("3 <- Average happiness level")
            print("4 <- Details on all dictionaries/lists")
            choice = -1
            try:
                choice = int(input())
            except:
                ValueError
            while isinstance(choice, int) == False or choice < 1 or choice > 4:
                print("Please enter a valid choice")
                try:
                    print("1 <- Working employees to total")
                    print("2 <- Average salary and whether you pay"
                          + " more than you profit")
                    print("3 <- Average happiness level")
                    print("4 <- Details on all dictionaries/lists")
                    choice = int(input())
                except:
                    ValueError
            if choice == 1:
                print(self.employInfo(returnVal = 1, numEmp = num_emp))
            if choice == 2:
                print(self.employInfo(returnVal=2, total_profit=profit_earned))
            if choice == 3:
                print(self.employInfo(returnVal = 3))
            if choice == 4:
                print("Salaries: ")
                self.getAll()
    #used to automatically pay salaries from a budget amount
    def paySal(self, budget):
        """Pays salaries of all employees. Runs at the end of each day

        Args:
            budget (int): a budget value indicating our total funds

        Returns:
            totalPay: the total salary to pay for all employees
        """
        totalPay = 0
        for name in self.salaries:
            totalPay += self.salaries[name]
        return totalPay
    #used to get the salaries dictionary
    def getSal(self):
        """Gets the salary attribute containing all employees and their salaries
        Side effects:
            prints out the name and salaries of all employees onto the console
        """
        print("Salaries: ")
        for name in self.salaries:
            print(f"{name}: ", self.salaries[name])
    #used to get all details on all dictionaries/lists
    def getAll(self):
        """Gets all attributes with names, salaries, and happiness
        Side effects:
            prints out the salary attribute dictionary, name list, 
            and happiness value
        """
        print("Employee names:", self.employeenames)
        #print("Employee ids: ", self.employee_ids)
        print("Employee salaries: ", self.salaries)
        print("Employee happiness: ", self.happiness)
    def numEmp(self):
        """Returns the number of employees working on a day

        Returns:
            int: the number of employees working
        """
        return len(self.employeenames) * (self.happiness/100)
        
    #used by the manageEmploy method to return different
    # information on employees
    def employInfo(self, returnVal = 1, total_profit = 0, numEmp = 0):
        """A method that returns a comparison of employee values to the 
        status of the store

        Args:
            returnVal (int, optional): A value indicating the user choice.
            Defaults to 1.
            total_profit (int, optional): the total profit made. Defaults to 0.
            numEmp (int, optional): the number of employees working on a 
            particular day. Defaults to 0.

        Returns:
            underMsg (str): less than half the employees worked if returned
            overMsg (str): over half the employees worked if returned
            salpro (str): Average salary is greater than average profit
            prosal (str): Average profit is greater than average salary
            wellhap (str): Average happiness is well
            lowhap (str): Average happiness is low
        Side effects:
            prints out conditions based on the returnVal given and the 
            comparisons made
        """
        if returnVal == 1:
            print(f"Number of working employees: {int(numEmp)}"
                  f" out of {len(self.employeenames)}")
            underMsg = "Less than half your employees worked today."
            overMsg = "More than half your employees worked today."
            return underMsg if (numEmp < len(self.employeenames)/2) else overMsg
        if returnVal == 2:
            total_sal = 0
            for name in self.salaries:
                total_sal += self.salaries[name]
            avg_sal = total_sal / len(self.employeenames)
            avg_profit = total_profit / len(self.employeenames)
            print("Average salary: ", avg_sal)
            print("Average profit per employee: ", avg_profit)
            salpro = "Your average salary pay is greater than profit"
            prosal = "Your average salary pay is less than profit per employee."
            return salpro if (avg_sal > avg_profit) else prosal
        if returnVal == 3:
            print("Employee happiness is: ", self.happiness)
            wellhap = "Your average happiness is doing well"
            lowhap = "Your employee happiness is pretty low."   
            return wellhap if (self.happiness > 50) else lowhap     
    

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
    """Runs a full simulation game, over a series of 
            game days.
        Args:
            EmployeeFilePath (str): a string containing the path to a file
            StockFilePath (str): a string containg the path to a file
                
        Side effects: Prints the game result to the terminal. 
    """
    dfmainTracker = pd.DataFrame(columns = ['Type','Day', 'Counter'])
    profit = 0
    dayCounter = 1
    fundsCounter = 1000
    dfmainTracker = dfmainTracker.append({'Type':1, 'Day':dayCounter, 
                                    'Counter':fundsCounter}, ignore_index=True)
    dfmainTracker = dfmainTracker.append({'Type':2, 'Day':dayCounter, 
                                          'Counter':profit}, ignore_index=True)
    #simlation runs for 5 days. 
    max_days = 5
    empNum = input("How many employees do you want? Max 10 \n")
    try:
        empNum = int(empNum)
    except:
        ValueError
    while isinstance(empNum, int) == False or empNum <= 0 or empNum >= 10:
        print("Please enter a valid number of employees. Max 10")
        try:
            empNum = int(input("How many employees do you want?"))
        except:
            ValueError
    employee = Employees(empNum, EmployeeFilePath)
    print("Your employees: ")
    print("Employee names:", employee.employeenames)
    print("Employee salaries: ", employee.salaries)
    print("Employee happiness: ", employee.happiness)
    print(input("Press enter to continue"))
    
    #populate inventory with the available stock
    inventory = read_stock(StockFilePath)
    
    #continues looping and running the simulation until the player 
    #completes 5 days or runs out of money
    while dayCounter < max_days + 1 and fundsCounter > 0:
        dayCounter, fundsCounter, profit, inventory = run_day(dayCounter,
                                                              fundsCounter,
                                                              profit,inventory,
                                                              employee)
        dfmainTracker = dfmainTracker.append({'Type':1, 'Day':dayCounter, 
                                              'Counter':fundsCounter},
                                             ignore_index=True)
        dfmainTracker = dfmainTracker.append({'Type':2, 'Day':dayCounter, 
                                              'Counter':profit},
                                             ignore_index=True)
        print("Final employee info:")
        print("Employee names:", employee.employeenames)
        print("Employee salaries: ", employee.salaries)
        print("Employee happiness: ", employee.happiness)
        print(input("Press enter to continue"))
    #player loses if they run out of money
        if fundsCounter <= 0:
            print(f"""Sorry, you ran out of money after day {dayCounter - 1}""")
            
    #return either a win message or a lose message after 5 days. 
    #win condition is currently $500 dollars profit
    if profit >= 500 * empNum:
        print(f'''Congratulations, you won the game. You made
                ${profit} in 5 days''')
    else:
        print(f'''Sorry, you lost the game. You only made 
                ${profit} in 5 days.''')
    return dfmainTracker
        
        
def run_day(day, funds, profit, inventory, employeeObj):
        """Prints store status, calls the store simulation method, then
        increases the day.
        
        Args:
            day (int): the current day of the simulation
            funds (inst): the current amount of funds the player has
            profit (int): the profit the player has made so far
            inventory (dict): a dict with a tuple as a key and a int as a 
                value. the store's inventory
            employeeObj (Employee): an Employees object containing employee
                information
        
        Side effects: 
            Prints information to the terminal for the player to 
            see store status
        """
        #give player store status
        print(f'''Welcome to day {day}. Here is the status of your 
              store:''')
        print(input("Press enter to continue"))
        #print finances
        print(f'''Your profit so far is ${profit}''')
        print(f'''Your current funds are ${funds}''')
        print(input("Press enter to continue"))
        #print inventory
        print('''Here is an overview of your current store inventory:''')
        
        #print each item 
        itemindex = 0
        itemslist = list(inventory)
        while itemindex < 15:
            item = itemslist[itemindex]
            print(f'Item: {item[0]}, Price: ${item[1]}, Quantity: \
                  {inventory[itemslist[itemindex]]}')
            itemindex += 1

        #simulation will now run
        print(input("Press enter to continue"))
        print(f'''The simulation for day {day} will now run''')
                
        #run a simulation of customers buying items in the store for a day
        inventory, sim_profit, workingEmp = simulate_day(inventory,profit, 
                                                         employeeObj)
        print("Funds before salaries: ", funds)
        salaries_paid = employeeObj.paySal(funds)
        funds -= salaries_paid
        print(f"You have paid {salaries_paid} in salaries.")
        print("Funds after paying salaries: ", funds)
        print(input("Press enter to continue"))
        while input("Would you like to manage employees?" +
                    " Y/Yes for yes \n").upper() in yeses:
            print("What would you like to do with employees?")
            print("0 <- Pay extra")
            print("1 <- Adjust salaries")
            print("2 <- Add employee")
            print("3 <- Get employee info")
            print("4 <- Get salaries")
            print("5 <- Nothing")
            choice = -1
            try:
                choice = int(input())
            except:
                ValueError
            while isinstance(choice, int) == False or choice < 0 or choice > 5:
                print("Please enter a valid choice")
                try:
                    print("What would you like to do with employees?")
                    print("0 <- Pay extra")
                    print("1 <- Adjust salaries")
                    print("2 <- Add employee")
                    print("3 <- Get employee info") 
                    print("4 <- Get salaries")
                    print("5 <- Nothing")
                    choice = int(input("Please enter your choice:\n"))
                except:
                    ValueError
            if choice == 0:
                funds = employeeObj.manageEmploys(budget = funds)
            if choice == 1:
                employeeObj.manageEmploys(val = 1)
            if choice == 2:
                funds = employeeObj.manageEmploys(budget = funds, val = 2)
            if choice == 3:
                employeeObj.manageEmploys(val = 3, profit_earned = sim_profit,
                                          num_emp = workingEmp)
            if choice == 4:
                employeeObj.getSal()
            if choice == 5:
                break
                

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
    
    num_employees = int(employeeObj.numEmp())
    maxcustomers = int(num_employees * 15)
    print("Maximum customers: ", maxcustomers)
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
                the previous amount was {currentamount}. \
                the new amount is {newamount}. profit is now ${profit}.""")
    return inventory, profit, num_employees
    
def main(EmployeeFilePath, StockFilePath):
    ''' Starts the game using the employee names and stock items.
    Args:
        EmployeeFilePath(str): the directory of the text file containing the
        names of employees
        StockFilePath(str): the directory of the text file containing the
        stock items and their prices
    Side effects:
        prints prompts and information to console for user to see
        prints end message for the user at end of game.
    '''
    graph_info = run_game(EmployeeFilePath, StockFilePath)
    print("Would you like to display graphs?")
    print("1 <- Funds during the game")
    print("2 <- Profit during the game")
    print("Any other key <- Don't show graphs")
    choice = input()
    GraphFilter(graph_info, choice)
    print("Thank you for playing!")  
    
def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("EmployeeList", help = "Excel file of employees")
    parser.add_argument("StockList", help = "Text file of stock and prices")
    return parser.parse_args(arglist)    

if __name__ == "__main__":
    args  = parse_args(sys.argv[1:])
    main(args.EmployeeList, args.StockList)