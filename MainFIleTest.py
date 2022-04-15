<<<<<<< HEAD

placeHolderItems = {"Milk": 3.30, "Meat": 5.00, "Cereal":4.00}
class employee():
    def __init__(self, name, salary, schedule):
        self.name = name
        self.salary = salary
        self.schedule = schedule
        
=======
>>>>>>> cec4b2fa1038420e5849aecf5908f281967a9bd7
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
<<<<<<< HEAD
    def setPrices(self, InventorySelection, newPrice):
        print("Current Store prices for inventory items")
        [print("lineItem\n") for lineItem in placeHolderItems]
        changeprice1 = input("Which item would you like to change to?")
        NewPrice = placeHolderItems.get(changeprice1) 
        placeHolderItems[f"{InventorySelection}"] = NewPrice
        placeHoldCont = input(f"{InventorySelection} New Price Set: {newPrice}")
    
=======
            
>>>>>>> cec4b2fa1038420e5849aecf5908f281967a9bd7
