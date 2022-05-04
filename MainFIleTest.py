from re import L
import random
import pandas as pd
placeHolderItems = {"Milk": 3.30, "Meat": 5.00, "Cereal":4.00}
class Employee():
    '''Creates the Employee class. 
    Attributes:
        name (str): the name of the employee
        salary (int): the salary of the employee
        schedule (dict): the schedule of the employee. the keys are ints 
            which represent the days of the week, from 1-7. the values
            are ints of 0 or 1, depending on whether the employee is working. 
            a value of 0 represents an off day, and a value of 1 represents
            a working day
    '''
    def __init__(self, num_employees, filename = ["Simon"]):
        #print("How many employees do you want?")
        #num_employees = input()
        #while(type(num_employees) != int):
        #    print("That is not a valid number. Please pick a number.")
        #    num_employees = input()
        employee_names = dict()
        employee_ids = list()
        #the names in the employee_names are the keys to the salary_dict
        salary_dict = dict()
        schedule_dict = dict()
        nameslist = list()
        happiness = dict()
        
        for i in range(num_employees):
            employee_ids.append(i)
            salary_dict[i] = 100
            happiness[i] = 65
            schedule_list = list()
            for j in range(14):
                schedule_list.append(random.randint(0, 1))
            schedule_dict[i] = schedule_list
        
        #self.names = employee_names
        self.employee_ids = employee_ids
        self.salaries = salary_dict
        self.schedules = schedule_dict
        self.happiness = happiness
        
    #def getnames(self):
    #    return self.names
    def getids(self):
        return self.employee_ids
    def getsal(self, id, all = False):
        if all == False:
            return self.salaries[id]
        else:
            return self.schedules
    def getschedule(self, id, all = False):
        if all == False:
            return self.schedules[id]
        else:
            return self.schedules
    def autofire(self):
        self.employees = [self.happiness[i] for i in range(len(self.happiness)) if self.happiness[i] > 70]
    def __init__(self, name, salary):
        ''' Initializes the attributes for the Employee object.
        Args:   
            name(str): the name of the employee
            salary(int): the salary of the employee
            schedule(dict): the schedule of the employee
        Side effects:
            sets the attribute values for the Employee object
        '''
        self.name = name
        self.salary = salary
        print("Please schedule 1 for yes or 0 for no for days this employee will be working.")
        schedule = dict()
        for i in range(14):
            print(f"Day {i}:")
            schedule[i] = input()
        self.schedule = schedule
        
    def __add__(self, other):
        
        return other - self.salary
    def pay_salary(self, budget):
        """_summary_

        Args:
            budget (double/int): a value indicating the amount of funds availible to pay employees

        Returns:
            (double/int)): the amount of funds left over after paying this employee salary
        """
        return budget - self.salary
    def __inv__(self, day):
        print("Which day would you like to change?")
        print(self.schedule)
        day = input()
        self.schedule[day] == "1" if self.schedule[day] == "0" else "0"
        return Employee(self.name, self.salary, self.schedule)
    #same as __inv__ but not a magic method
    def upd_schedule(self):
        while(True):
            print(self.schedule)
            print(f"Would you like to update {self.name}'s schedule? Y/N")
            change = input()
            if change == "Y":
                print("Which day would you like to change?")
                print(self.schedule)
                changeday = input()
                self.schedule[changeday] == "1" if self.schedule[changeday] == "0" else "0"
        
class Boss(Employee):
    ''' Creates the class Boss, a subclass of Employee
    '''
class Manager(Employee):
    ''' Creates the class Manager, a subclass of Employee
    '''
class Worker(Employee):
    '''Creates the class Worker, a subclass of Employee
    '''
    
class Player():
    '''Creates the Player class.
    Attributes:
        name (str): the name of the player
        score (int): the score achieved by the player, which is their profit
    '''
    def __init__(self, name, score=0):
        '''Initializes the attributes of the Player object.
        Args:
            name(str): the name of the player
            score(int): the profit made by the player. the default value
            is 0
        Side effects:
            Initializes the attributes name and score'''
        self.name = name
        self.score = score
        
class Store():
    ''' Creates the Store class.
    Attributes:
        name(str): the name of the player
        funds(int): the funds available for the player
        size():
        inventory(): the inventory of the player
    '''
    def __init__(self,name, Funds, size, inv):
        ''' Initializes the attributes for the Store object.
        Args:
            name (str): the name of the player
            funds (int): the funds available to the player
            size():
            inv(): the current inventory of the player's store
        Side effects:
            sets the values of the attributes of the Store object
        '''
        self.name = name
        self.funds = Funds
        self.size = size
        self.inventory = inv
    def buyInventory(self, InvItem, amountPurchased):
        '''Purchases items for the player's inventory.
        Args:
            InvItem(str): the item being purchases
            amountPurchased(int): the amount of the item being purchased
        Returns:
            amountPurchased(int): the amount of the item purchased
        Side effects:
            prints message to console for player
        '''
        stockBuying = placeHolderItems.get(InvItem) * amountPurchased
        confirmPurchase = input(f"Your currently purchasing {amountPurchased} \
                                of {InvItem}, this will cost you {stockBuying}\
                                , which will reduce store funds to \
                                {self.funds - stockBuying} (Y/N)")
        if confirmPurchase.upper() == "Y":
            print(f"purchased {amountPurchased} {InvItem}")
            return amountPurchased
        else:
            print("Purchased declined")
    def setPrices(self, InventorySelection, newPrice):
        ''' Sets the prices of the items in the player's inventory.
        Args:
            InventorySelection(str): the item in the inventory
            newPrice(int): the new price that is being set
        Side effects:
            prints message for player to console
        '''
        print("Current Store prices for inventory items")
        [print("lineItem\n") for lineItem in placeHolderItems]
        changeprice1 = input("Which item would you like to change to?")
        NewPrice = placeHolderItems.get(changeprice1) 
        placeHolderItems[f"{InventorySelection}"] = NewPrice
        placeHoldCont = input(f"{InventorySelection} New Price Set: {newPrice}")


def mainGame(optionsList = []):
    ''' Shows the options for the player to choose from for each turn
    Args:
        optionsList(list): the list of selections the player
        can choose from
    Side effects:
        prints the different choices the player can make
    '''
    print("Main Game Menu")
    [print(optionsList.index(item)," ", item) for item in optionsList]
    
print mainGame([])

class Store():
    def __init__(self, start_rent, max_inv):
        """Initializes the attributes for the Store class.
        
        Args: 
            start_rent (int): the amount of rent for the store.
            max_inv (int): the maximum number of items that can be in 
                the player's inventory.
        
        Side effects:
            Initializes the attributes profit, money, inv, prices, rent, max_inv.
        """
        self.profit = 0
        self.money = 1000
        self.inv = {}
        self.prices = {}
        #self.salary = salary
        self.rent = start_rent
        self.max_inv = max_inv
        
    def buy_inventory(self, wholesale_stock):
        """
        Allows the player to buy items for their store inventory from a  
            wholesale inventory. 
        
        Args: 
            wholesale_stock (dict {string:float}): the items available
            for the player to purchase for their store. Structure of the 
            dictionary is {"item name":<unit price>}. 
        
        Returns:
            inv (dict {string:int}): a dictionary of the items a player 
                has in their store inventory. Structure of the dictionary
                is {"item name":<quantity of item in inventory>}.
        
        Side effects:
            Can modify the attributes money and inv.  
        """
        pass
    
    def set_prices(self):
        """Allows the player to set the prices for items in their store.
        
        Side effects: 
            Prints instructions and information to the terminal for the player
                to set prices interactively.
            Can modify the prices attribute. 
        """
        pass
    
    def manage_expenses(self):
        """Allows the user to manage employee salaries and view store rent. 
        
        Side effects:
            Prints instructions and information to the terminal for the player
                to manage employee salaries interactively.
        """
        pass
    
class GameState():
    """A class that can run a full store simluation game.
    
    Attributes:
        day (int): the current day of the simulation.
        wholesale_stock (dict {string:float}): the items available
            for the player to purchase for their store. Structure of the 
            dictionary is {"item name":<unit price>}.
        store (Store): the Store object that the simulation will run on.
    """
    
    def __init__(self, start_rent, max_inv, products):
        """Initializes the GameState object attributes and establishes the 
        stock avaliable to purchase during the simulation.
        
        Args:
            products (string): a file path to a document of the items available
            for the player to purchase for their store.
            
        Side effects:
            Initializes the attributes day, store, and wholesale_stock.
        """
        #day is set to 1 because the day counter increases at the end of 
        # each day
        self.day = 1
        #create store object
        self.store = Store(start_rent, max_inv)
        #initialize wholesale_stock as an empty dictionary
        wholesale_stock = {}
        
    
    def run_game(self):
        """Runs a full simulation game on a Store object, over a series of 
            game days.
            
            Args: 
                store (Store): a Store object.
                
            Side effects: Prints the game result to the terminal. 
        """
        #populate the wholesale_stock attribute with the available stock
        self.read_stock(self.store)
        
        #continues looping and running the simulation until the player 
            #completes 14 days or runs out of money
        while self.day < 15:
            #player loses if they run out of money
            if self.store.funds == 0:
                print(f'Sorry, you ran out of money after day {self.day - 1}')
                return
            #halfway through the 14 days (beginning of day 8), employee salaries 
            # are deducted from player funds
            if self.day == 8:
                #still need to implement: remove the amount of salary of all 
                #the employees from the total funds in the store object. 
                print(f'''It\'s employee payday. Employee salaries have 
                      been deducted from your store funds. Your current funds
                      are now {self.store.funds}''' )
            #run one day simulation
            self.store = self.run_day(self.store)
        
        #return either a win message or a lose message after 14 days. 
        #we can edit the win condition but for now I put $500 in profit
        if self.store.profit >= 500:
            print(f'''Congratulations, you won the game. You made
                  ${self.store.profit} in 14 days''')
            return
        else:
            print(f'''Sorry, you lost the game. You only made 
                  {self.store.profit} in 14 days.''')
            return
              
    
    def read_stock(self, store):
        ''' reads a file that determines the wholesale stock available. 
        opens the file using a with statement and reads with regex.
        Args:
            store(Store): a store object.
        Side effects:
            adds the wholesale stock names and prices into the
            wholesale_stock dictionary, with the item names as the
            keys and the prices as the values.
        '''
        with open("storestock.txt", "r", encoding = "utf-8") as f:
            expr = (r"""(?gm)
                    ^
                    (?:(?P<item>[a-z]+)*\s)
                    (?P<price>\d*)""")
            for line in f:
                stock_item = re.search(expr, line)
                if stock_item:
                    stockname = stock_item.group("item")
                    stockprice = stock_item.group("price")
                    self.wholesale_stock[stockname] = stockprice
    
    def run_day(self,store):
        """Runs one day of the simulation on a Store object. One day includes
            the user managing the store's inventory and finances before the day, 
            then simulated customers purchasing items that day.
            
        Args:
            store (Store): a Store object.
            
        Returns:
            store (Store): a Store object.
            
        Side effects: 
            Prints information to the terminal for the player to
                manage the store and see the results of the day.
            Can modifiy the attribute day.
        """
        #print the store status to the player
        self.store_status(self.store)
        
        while True:
            manage_store = input(f'''Type "B" to buy more inventory, type "P" 
                                 to change inventory prices, or type "E" to 
                                 manage store expenses. When finished, type "S"
                                 to run store simulation. 
                                 ''')
            if manage_store.upper() == 'B':
            #print to user to ask if they want to buy more inventory, and call
                #buy_inventory method. we may need to add to the buy_inventory or
                #add another method that allows the player to select which items
                #they want to buy. 
                continue
            
            if manage_store.upper() == 'P':
            #print to user to ask if they want to change inventory prices, and
                #call set_prices method. we may need to add to the set_prices
                #method or add a new method to allow the player to select which 
                # items they want to change the price of.
                continue
            
            if manage_store.upper() == 'P':
            #print to user to ask if they want to manage store expenses. If yes,
                #then go to manage_expenses method.
                continue
                
            if manage_store.upper() == 'S':
                break
        
        #run a simulation of customers buying items in the store for a day
        self.store = self.simulate_day(self.store)
        
        #increase the day variable
        day += 1
        
        return self.store
                   
    
    def simulate_day(self, store):
        """Runs the customer purchasing simulation activities for one 
            game day. The purchasing simulation is mainly random but may be 
            influenced by certain external events in the game.
            
            Args: 
                store (Store): a Store object.
                
            Returns: 
                store (Store): a Store object. 
            
            Side Effects:
                Can modify the attributes profit and money.
            """
        customercount = random.randint(1,30)
        # for each customer
        for person in range(len(customercount)):
            itemslist = list(self.wholesale_stock.keys())
            itemslist[random.randint(1,)]
            # gets list of items
            itemslist = list(self.inv.keys())
            # gets a random int for the purchase and buys what is at
            # that index
            purchase = itemslist[random.randint(1,15)]
            # gets the current amount of the item
            currentamount = self.inv.get(purchase)
            # subtracts the purchase from the total
            self.inv[purchase] = currentamount - 1
            # updates profit
            self.profit += self.prices.get(purchase)
        # if it is a rent payment day, pays the rent
        if pay_rent == True:
            self.money -= self.rent
        # if it is an employee payment day, pays the employee
        if pay_salary == True:
            self.money -= self.salary

        return self.store
    
    def store_status(self, store):
        """Prints the properties of the store to the player.
        
        Args:
            store (Store): a Store object.
            
        Side effects:
            Prints the store propeties to the terminal. 
        """
        # use __str__ here
        pass

#types of days
def event():
    ''' Randomly decides if the day will have a random event. 
    If yes, then it will randomly select a random event for that day,
    and execute it.
    '''
    events = []
    dayType = random.randint(0, len(events))
  
if __name__ == "__main__":
    pass
#==========================================================================================
