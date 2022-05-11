from argparse import ArgumentParser
import sys
import re
import random

#python .\StoreSim.py AAAA "EmployeeTest.xlsx" "storestock.txt"

def main(storeName, EmployeeFilePath, StockFilePath):
    print("SSSSSSSSSSSSS")
    print(storeName)
    print(EmployeeFilePath)
    #run the game
    run_game(StockFilePath)

def read_stock(filename):
    ''' reads a file that sets the items, prices, and stock.
    opens the file using a with statement and reads with regex.
    Args:
        store(Store): a store object.
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
    
def run_game(StockFilePath):
        profit = 0
        dayCounter = 1
        fundsCounter = 1000
        """Runs a full simulation game, over a series of 
            game days.
                
            Side effects: Prints the game result to the terminal. 
        """
        #populate inventory with the available stock
        inventory = read_stock(StockFilePath)
        
        #continues looping and running the simulation until the player 
        #completes 5 days or runs out of money
        while dayCounter < 6 and fundsCounter > 0:
            run_day(dayCounter, fundsCounter, profit, inventory)
        
        #return either a win message or a lose message after 14 days. 
        #we can edit the win condition but for now I put $500 in profit
        if profit >= 500:
            print(f'''Congratulations, you won the game. You made
                  ${profit} in 5 days''')
            
        else:
            print(f'''Sorry, you lost the game. You only made 
                  {profit} in 5 days.''')
        
        
def run_day(day, funds, profit, inventory):
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
        #print each item using a list comprehension
        [print(f'''Item: {inv_item[0]}, Price: {inv_item[1]}, Quantity: {inventory[inv_item]}''') for inv_item in inventory]

        #simulation will now run
        print(f'''The simulation for day {day} will now run''')
                
        #run a simulation of customers buying items in the store for a day
        simulate_day(inventory)
        
        #increase the day variable

def simulate_day(inventory):
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
    customercount = random.randint(1,30)
    itemslist = list(inventory.keys())
    for person in range(customercount):
        itemindex = random.randint(1, 15)
        purchase = itemslist[itemindex]
        price = purchase[1]
        currentamount = inventory.get(purchase)
        inventory[itemindex] = currentamount - 1
        profit += price

    
def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("StoreName", help="Name of the store")
    parser.add_argument("EmployeeList", help = "Excel file of employees")
    parser.add_argument("StockList", help = "The text file of the stock for the store")
    return parser.parse_args(arglist)    

if __name__ == "__main__":
    args  = parse_args(sys.argv[1:])
    main(args.StoreName, args.EmployeeList, args.StockList)