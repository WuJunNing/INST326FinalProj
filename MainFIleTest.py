#====================================================================================
#Luis Gomez Code Part
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
        self.name = name
        self.salary = salary
        self.schedule = schedule
class Player():
    '''Creates the Player class.
    Attributes:
        name (str): the name of the player
        score (int): the score achieved by the player, which is their profit
    '''
class Store():
    def __init__(self,name, Funds, size, inv):
        self.name = name
        self.funds = Funds
        self.size = size
        self.inventory = inv
    def buyInventory(self, InvItem, amountPurchased):
        stockBuying = placeHolderItems.get(InvItem) * amountPurchased
        confirmPurchase = input(f"Your currently purchasing {amountPurchased} of {InvItem}, this will cost you {stockBuying}, which will reduce store funds to {self.funds - stockBuying} (Y/N)")
        if confirmPurchase.upper() == "Y":
            print(f"purchased {amountPurchased} {InvItem}")
            return amountPurchased
        else:
            print("Purchased declined")
    def setPrices(self, InventorySelection, newPrice):
        print("Current Store prices for inventory items")
        [print("lineItem\n") for lineItem in placeHolderItems]
        changeprice1 = input("Which item would you like to change to?")
        NewPrice = placeHolderItems.get(changeprice1) 
        placeHolderItems[f"{InventorySelection}"] = NewPrice
        placeHoldCont = input(f"{InventorySelection} New Price Set: {newPrice}")


def mainGame(optionsList = []):
    print("Main Game Menu")
    [print(optionsList.index(item)," ", item) for item in optionsList]
    
print mainGame([])
#=======
from re import L
import random

class Store():
    def __init__(self, start_rent, maxinv):
        """Initializes the attributes for the Store class.
        
        Args: 
            start_rent (int): the amount of rent for the store.
            maxinv (int): the maximum number of items that can be in 
                the player's inventory.
        
        Side effects:
            Initializes the attributes profit, money, inv, prices, rent, maxinv.
        """
        self.profit = 0
        self.money = 1000
        self.inv = {}
        self.prices = {}
        #self.salary = salary
        self.rent = start_rent
        self.maxinv = maxinv
        
    def buy_inventory(wholesale_stock):
        """
        Allows the player to buy items for their store inventory from a  
            wholesale inventory. 
        
        Args: 
            wholesale_stock (dictionary {string:float}): the items available
            for the player to purchase for their store. Structure of the 
            dictionary is {"item name":<unit price>}.
        
        Returns:
            inv (dictionary {string:int}): a dictionary of the items a player 
                has in their store inventory. Structure of the dictionary
                is {"item name":<quantity of item in inventory>}.
        
        Side effects:
            can modify the variables money and inv.  
        """
        pass
    def set_prices():
        pass
    def manage_expenses():
        pass
    
class GameState():
    """A class that can run a full store simluation game.
    
    Attributes:
        day (int): the current day of the simulation.
        wholesale_stock (dictionary {string:float}): the items available
            for the player to purchase for their store. Structure of the 
            dictionary is {"item name":<unit price>}.
    """
    
    def __init__(self, products):
        """Initializes the GameState object attributes and establishes the 
        stock avaliable to purchase during the simulation.
        
        Args:
            products (dictionary {string:float}): the items available
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
            Can modifiy the variables inv, emp_sal, profit, and funds.
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
                Can modify the variables profit and money.
            """
        pass
    
    def store_status(self, store):
        """Prints the properties of the store to the player.
        
        Args:
            store (Store): a Store object.
            
        Side effects:
            Prints the store propeties to the terminal. 
        """
        pass

#types of days
def event():
    events = []
    dayType = random.randint(0, len(events))
#employee class with subclasses for different positions
class employee():
    def __init__(salary, position):
        self.salary = salary
        self.position = position
        
class boss():
class manager():
class worker():
    
if __name__ == "__main__":
    pass
    

        
        

#==========================================================================================