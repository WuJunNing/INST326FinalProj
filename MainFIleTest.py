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
        store (Store): the Store object that the simulation will run on.
    """
    
    def __init__(self, funds, max_inv, products):
        """Initializes the GameState object attributes and establishes the 
        stock avaliable to purchase during the simulation.
        
        Args:
            funds (int): the starting funds for the player
            products (string): a file path to a document of the items available
            for the player to purchase for their store.
            
        Side effects:
            Initializes the attributes day, store, and wholesale_stock.
        """
        #day is set to 1 because the day counter increases at the end of 
        # each day in the run_day method
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
        #opens the file of wholesale items and their prices
        with open("storestock.txt", "r", encoding = "utf-8") as f:
            #sets the regular expression to be used
            expr = (r"""(?gm)
                    ^
                    (?:(?P<item>[a-z]+)*\s)
                    (?P<price>\d*)""")
            #iterates over each line in the document
            for line in f:
                #uses regex to search for matches
                stock_item = re.search(expr, line)
                #if there is a match
                if stock_item:
                    #sets item name and price based on regex group name
                    stockname = stock_item.group("item")
                    stockprice = stock_item.group("price")
                    #adds item and price to dictionary
                    #with item name as the key and price as the value
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
        
        #acceptable characters to input
        manage_options = ['B', 'b', 'P', 'p','E', 'e', 'S', 's']
        
        while True:
            manage_store = input(f'''Type "B" to buy more inventory, type "P" 
                                 to change inventory prices, or type "E" to 
                                 manage store expenses. When finished, type "S"
                                 to run store simulation. 
                                 ''')
            #if player types in an option that is not acceptable
            if manage_store not in manage_options:
                print('''f{manage_store} is not one of the options please 
                      choose one of the following options''')
                continue
                
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
            
            if manage_store.upper() == 'E':
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
        #gets a random total num of customers for that day
        customercount = random.randint(1,30)
        for person in range(len(customercount)):
            itemslist = list(self.wholesale_stock.keys())
            itemslist[random.randint(1,)]
        # if it is a rent payment day, pays the rent
        if pay_rent == True:
            self.money -= self.rent
        # if it is an employee payment day, pays the employee
        if pay_salary == True:
            self.money -= self.salary
        
    
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