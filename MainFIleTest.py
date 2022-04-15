class Store():
    def __init__(self, Funds, size, inv):
        self.funds = Funds
        self.size = size
        self.inventory = inv
    def buyInventory(self, InvItem, amountPurchased):
        placeHolderItems = {"Milk": 3.30, "Meat": 5.00, "Cereal":4.00}
        stockBuying = placeHolderItems.get(InvItem) * amountPurchased
        confirmPurchase = input(f"Your currently purchasing {amountPurchased} of {InvItem}, this will cost you {stockBuying}, which will reduce store funds to {self.funds - stockBuying} (Y/N)")
        if confirmPurchase.upper() == "Y":
            print(f"purchased {amountPurchased} {InvItem}")
            return amountPurchased
        else:
            print("Purchased declined")
            
