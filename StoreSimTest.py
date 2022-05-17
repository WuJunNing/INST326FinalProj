from argparse import ArgumentParser
import sys
import re
import random

#python .\StoreSim.py AAAA "EmployeeTest.xlsx" "storestock.txt"
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
        
        #opens a text file of names and fills employee_names with names in order equal to the number chosen by the player
        with open(filename, "r", encoding = "utf-8") as f:
            curr_count = 0
            for name in f:
                name = name[:-2]
                if curr_count < num_employees:
                    employee_names.append(name)
                    curr_count += 1
                else:
                    break
                
        #For each employee, an id is assigned in order starting from 0
        #A random salary from 1 to 10 and happiness from 65 to 75 is given
        #A list with the days argument as the max value is set for each name key        
        for i in range(len(employee_names)):
            employee_ids[i] = employee_names[i]
            salary_dict[employee_names[i]] = random.randint(1, 10)
            happiness[employee_names[i]] = random.randint(65, 75) #values adjusted
            schedule_list = list()
            for j in range(days):
                schedule_list.append(random.randint(0, 1))
            schedule_dict[employee_names[i]] = schedule_list
            
        #assigned attributes
        self.employeenames = employee_names
        self.employee_ids = employee_ids
        self.salaries = salary_dict
        self.schedules = schedule_dict
        self.happiness = happiness
        
    def manageEmploys(self, val = 0, budget = 0, profit_earned = 0, a_day = 0):
        #val == 0 multiples a player salary and happiness and subtracts from funds a certain amount equal to the new salaries
        if val == 0:
            total_pay = 0
            for name in self.employeenames:
                if input(f"Would you like to pay {name} an extra salary? 1.5 multiplier on salary. Y = Yes, anything else = no") == "Y":
                    print(self.happiness[name])
                    self.happiness[name] += 10
                    print(self.happiness[name])
                    print(self.salaries[name])
                    self.salaries[name] *= 1.5
                    print(self.salaries[name])
                    total_pay += self.salaries[name]
            return budget - total_pay
        
        #val == 1 loops as long as the player wants to adjust salary
        if val == 1:
            while(input("Would you like to keep changing salaries? Y for yes") == "Y"):
                print(self.salaries)
                emp_name = input("Which employee do you want to change the salary of? Type in a name.")
                curr_sal = self.salaries[emp_name]
                self.salaries[emp_name] = int(input("What is their new salary?"))
                if curr_sal > self.salaries[emp_name]:
                    print(self.happiness[emp_name])
                    self.happiness[emp_name] /= 1.5
                    print(self.happiness[emp_name])
        #val == 2 adds a new employee
        if val == 2:
            print(budget)
            newemp = input("What is this new employee's name?")
            self.employeenames.append(newemp)
            self.employee_ids[len(self.employeenames) - 1] = newemp
            newsal = random.randint(1, 10)
            self.salaries[newemp] = newsal
            budget = budget - newsal
            newschedule = list()
            for i in range(a_day):
                newschedule.append(random.randint(0, 1))
            self.schedules[newemp] = newschedule
            self.happiness[newemp] = random.randint(80, 90)
            print(budget)
            return budget
        #val == 3 provides a selection of options where the player can get different information on the employees
        if val == 3:
            print("What information would you like?")
            print("1 <- Number of working employees")
            print("2 <- Average salary and whether you pay more than you profit")
            print("3 <- Average happiness level")
            print("4 <- Details on all dictionaries/lists")
            try:
                choice = int(input())
            except:
                ValueError
            while isinstance(choice, int) == False or choice < 1 or choice > 4:
                print("Please enter a valid choice")
                try:
                    choice = int(input())
                except:
                    ValueError
            if choice == 1:
                print("test1")
                print(self.employInfo(returnVal = 1, ex_val = 1, the_day = a_day))
            if choice == 2:
                print("test2")
                print(self.employInfo(returnVal = 2, total_profit = profit_earned, the_day = a_day))
            if choice == 3:
                print(self.employInfo(returnVal = 3))
            if choice == 4:
                self.getAll()
    #used to automatically pay salaries from a budget amount
    def paySal(self, budget):
        totalPay = 0
        for name in self.salaries:
            totalPay += self.salaries[name]
        return budget - totalPay
    #used to get the salaries dictionary
    def getSal(self):
        for name in self.salaries:
            print(f"{name}: ", self.salaries[name])
    #used to get all details on all dictionaries/lists
    def getAll(self):
        print("Employee names:", self.employeenames)
        print("Employee ids: ", self.employee_ids)
        print("Employee salaries: ", self.salaries)
        print("Employee schedules: ", self.schedules)
        print("Employee happiness: ", self.happiness)
    #used by the manageEmploy method to return different information on employees
    def employInfo(self, returnVal = 1, ex_val = 0, the_day = 0, total_profit = 0):
        if returnVal == 1:
            working = 0
            real_day = the_day
            print(real_day)
            for name in self.schedules:
                if self.schedules[name][real_day] == 1:
                    chance = random.randint(0, 100)
                    if chance <= self.happiness[name]:
                        working += 1
            if ex_val == 1:
                print(f"Number of working employees: {working} out of {len(self.employeenames)}")
            return working
        if returnVal == 2:
            total_sal = 0
            for name in self.salaries:
                total_sal += self.salaries[name]
            avg_sal = total_sal / len(self.employeenames)
            print(avg_sal)
            print(total_profit)
            return "Your average salary pay is greater than profit" if (avg_sal > total_profit) else "Your average salary pay is less than profit."
        if returnVal == 3:
            total_hap = 0
            for name in self.happiness:
                total_hap += self.happiness[name]
            avg_hap = total_hap / len(self.employeenames)
            print(avg_hap)
            return "Your average happiness is doing well" if (avg_hap > 50) else "Your employee happiness is pretty low."       
    
def main(storeName, EmployeeFilePath, StockFilePath):
    print("SSSSSSSSSSSSS")
    print(storeName)
    print(EmployeeFilePath)
    #run the game
    run_game(EmployeeFilePath, StockFilePath)

def read_stock(filename):
    ''' reads a file that sets the items, prices, and stock.
    opens the file using a with statement and reads with regex.
    Args:
        store(Store*): a store object.
    Side effects:
        creates inventory(dict), with keys being tuples of the
        item name and price, and values being the stock amount.
    '''
    #opens the file
    with open(filename, "r", encoding = "utf-8") as f:
        inventory = {}
        for line in f:
            expr = (r"""(?mx)
                    ^
                    (?:(?P<item>[a-z]+)*\s)
                    (?P<price>\d*)""")
            match = re.search(expr,line)
            if match:
                    # puts item name and price into list, which will be the key
                    # default inventory amount is 50, this is the value
                itemname = match.group("item")
                itemprice = match.group("price")
                itemlisting = (itemname, itemprice)
                inventory[itemlisting] = 50    
    return inventory        
    
def run_game(EmployeeFilePath, StockFilePath):
        PROFITLISTFORGRAPHING = []
        DAYCOUNTERLISTFORGRAPHINGX = []
        FUNDCOUNTERLISTFORGRAPHINGY = []
        profit = 0
        
        dayCounter = 0
        fundsCounter = 1000
        max_days = 0
        try:
            max_days = int(input("How many days do you want to try?"))
        except: 
            ValueError
        while isinstance(max_days, int) == False or max_days <= 0:
            print("Plase enter a valid number of days.")
            try:
                max_days = int(input("How many days do you want?"))
            except:
                ValueError
        empNum = 0
        try:
            empNum = int(input("How many employees do you want?"))
        except:
            ValueError
        while isinstance(empNum, int) == False or empNum <= 0:
            print("That is not a valid value. Please enter a number of employees.")
            try:
                empNum = int(input("How many employees do you want?"))
            except:
                ValueError
        employee = Employees(empNum, max_days, EmployeeFilePath)
        print("Employee names:", employee.employeenames)
        print("Employee ids: ", employee.employee_ids)
        print("Employee salaries: ", employee.salaries)
        print("Employee schedules: ", employee.schedules)
        print("Employee happiness: ", employee.happiness)
        """Runs a full simulation game, over a series of 
            game days.
                
            Side effects: Prints the game result to the terminal. 
        """
        #populate inventory with the available stock
        inventory = read_stock(StockFilePath)
        
        #continues looping and running the simulation until the player 
        #completes 5 days or runs out of money
        
        while dayCounter < max_days and fundsCounter > 0:
            dayCounter, fundsCounter, profit, inventory = run_day(dayCounter, fundsCounter, profit, inventory, employee, dayCounter)

            DAYCOUNTERLISTFORGRAPHINGX.append(dayCounter)
            FUNDCOUNTERLISTFORGRAPHINGY.append(fundsCounter)
            
            
        
        #return either a win message or a lose message after 14 days. 
        #we can edit the win condition but for now I put $500 in profit
        if profit >= max_days * 200:
            print(f'''Congratulations, you won the game. You made
                  ${profit} in {max_days} days''')
            
        else:
            print(f'''Sorry, you lost the game. You only made 
                  ${profit} in {max_days} days.''')
        print("Employee names:", employee.employeenames)
        print("Employee ids: ", employee.employee_ids)
        print("Employee salaries: ", employee.salaries)
        print("Employee schedules: ", employee.schedules)
        print("Employee happiness: ", employee.happiness)
        
def run_day(day, funds, profit, inventory, employeeObj, curr_day):
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
            
        
        #print(f'Item: {inventory}')
        
        
        #[print(f'''Item: {inv_item[0]}, Price: {inv_item[1]}, Quantity: {inventory[inv_item]}''') for inv_item in inventory]

        #simulation will now run
        print(f'''The simulation for day {day + 1} will now run''')
        
        #run a simulation of customers buying items in the store for a day
        inventory, profit = simulate_day(inventory,profit, employeeObj, curr_day)
        print("Before salaries: ", funds)
        funds = employeeObj.paySal(funds)
        print("Funds now: ", funds)
        while input("Would you like to manage employees? Y for yes/N for no") == "Y":
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
                    choice = int(input("What would you like to do with employees?"))
                    
                except:
                    ValueError
            if choice == 0:
                funds = employeeObj.manageEmploys(budget = funds)
            if choice == 1:
                employeeObj.manageEmploys(val = 1)
            if choice == 2:
                funds = employeeObj.manageEmploys(budget = funds, val = 2, a_day = curr_day)
            if choice == 3:
                employeeObj.manageEmploys(val = 3, profit_earned = profit, a_day = curr_day)
            if choice == 4:
                employeeObj.getSal()
            if choice == 5:
                break
       
        funds += profit
        #increase the day variable
        day += 1
        return day, funds, profit, inventory

def simulate_day(inventory,profit, employeeObj, curr_day):
    '''Runs the customer purchasing simulation activities for one 
    game day. The purchasing simulation is mainly random but may be 
    influenced by certain external events in the game.
                
    Args: 
        store (Store): a Store object.
        
    Returns: 
        store (Store): a Store object. 
    
    Side Effects:
        Can modify the attributes profit and money.
    '''
    maxcustomers = employeeObj.employInfo(1, the_day = curr_day) * 15
    print("Maximum customers: ", maxcustomers)
    customercount = random.randint(0,maxcustomers)
    print(f"{customercount} customer(s) came to the store today.")
    #customercount += employees * 15
    itemslist = list(inventory)
    for person in range(customercount):
        itemindex = random.randint(0, 14)
        purchase = itemslist[itemindex]
        print(f'item is {purchase[0]}')
        price = purchase[1]
        print(f'price is {price}')
        if inventory.get(purchase) == 0:
            continue
        currentamount = inventory.get(purchase)
        print(f'currentamount is {currentamount}')
        inventory[itemindex] = currentamount
        newamount = inventory[itemslist[itemindex]] = currentamount - 1
        print(f'new amount is {newamount}')
        profit += int(price)
        print(f"profit is {profit}")
        print(f"""customer {person + 1} bought 1 {purchase[0]} for ${price}.
        the previous amount was {currentamount}. the new amount is {newamount}.
        profit is now ${profit}.""")
    return inventory, profit
    
def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("StoreName", help="Name of the store")
    parser.add_argument("EmployeeList", help = "Excel file of employees")
    parser.add_argument("StockList", help = "The text file of the stock for the store")
    return parser.parse_args(arglist)    

if __name__ == "__main__":
    args  = parse_args(sys.argv[1:])
    main(args.StoreName, args.EmployeeList, args.StockList)