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
    def __init__(self, name, salary, schedule):
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
        self.schedule = schedule
        
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
    """
    
    def __init__(self, products):
        """Initializes the GameState object attributes and establishes the 
        stock avaliable to purchase during the simulation.
        
        Args:
            products (dict {string:float}): the items available
            for the player to purchase for their store. Structure of the 
            dictionary is {"item name":<unit price>}.
            
        Side effects:
            Initializes the attributes wholesale_stock and day.
        """
        self.day = 0
        self.wholesale_stock = products
        
    def run_game(self, store):
        """Runs a full simulation game on a Store object, over a series of 
            game days.
            
            Args: 
                store (Store): a Store object.
                
            Side effects: Prints the game result to the terminal. 
        """
        pass
    
    def read_stock(self, store):
        ''' reads a file that determines the wholesale stock available. 
        uses with statements and regex
        '''
        with open("storestock.txt", "r", encoding = "utf-8") as f:
            #regular expression goes here
            expr = ()
            for line in f:
                stock_item = re.search(expr, line)
                if stock_item:
                    stockname = stock_item.group()
                    stockprice = stock_item.group()
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
            Can modifiy the attributes inv, emp_sal, profit, and funds.
        """
        pass
    
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
        pass
    
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