#====================================================================================
#Luis Gomez Code Part
placeHolderItems = {"Milk": 3.30, "Meat": 5.00, "Cereal":4.00}
class employee():
    def __init__(self, name, salary, schedule):
        self.name = name
        self.salary = salary
        self.schedule = schedule
class player():
    
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
        
        self.profit = 0
        self.money = 1000
        self.inv = {}
        #self.salary = salary
        self.rent = start_rent
        self.maxinv = maxinv
    def buy_inventory():
        pass
    def set_prices():
        pass
    def manage_expenses():
        pass
class GameState():
    """A class that can run a full store simluation game."""
    def __init__(self, products):
        """Initializes the GameState object and establishes the stock avaliable
            to purchase during the simulation.
        
        Args:
            products (dictionary{string:float}): the list of items available
            for the player to purchase for their store.
            
        Side effects:
            Initializes the attributes wholesale_stock and day.
            """
        self.day = 0
        self.wholesale_stock = products
        
    def run_game(self):
        pass
    def run_day(self):
        pass
>>>>>>> 201f2ee452c2d79715485d1e1c61249b0201047b
    
    def simulate_day(self):
        pass
    def store_status(self):
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