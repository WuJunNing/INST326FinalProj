from argparse import ArgumentParser
import sys
import re

#python .\StoreSim.py AAAA "EmployeeTest.xlsx" "storestock.txt"

def main(storeName, EmployeeFilePath, StockFilePath):
    print("SSSSSSSSSSSSS")
    print(storeName)
    print(EmployeeFilePath)
    #run the game
    run_game(StockFilePath)

def read_stock(filename):
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
                    inventory[itemname] = itemprice              
    
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
            run_day(dayCounter)
        
        #return either a win message or a lose message after 14 days. 
        #we can edit the win condition but for now I put $500 in profit
        if profit >= 500:
            print(f'''Congratulations, you won the game. You made
                  ${profit} in 5 days''')
            
        else:
            print(f'''Sorry, you lost the game. You only made 
                  {profit} in 5 days.''')
        
        
def run_day(day, funds):
        """Prints store status, calls the store simulation method, then
        increases the day.
        
        Side effects: 
            Prints information to the terminal for the player to 
            see store status
            Can modifiy the day variable.
        """
        #give player store status
        print(f'''Welcome to day {dayCounter}. Here is the status of your 
              store:''')

        #print finances
        print(f'''Your profit so far is ${profit}''')
        print(f'''Your current funds are ${funds}''')

        #print inventory
        print('''Here is an overview of your current store inventory:''')
        #print each item using a list comprehension
        [print(f'''Item: {inv_item}, Price: {inventory[inv_item]}''') for inv_item in inventory]

        #simulation will now run
        print(f'''The simulation for day{dayCounter} will now run''')
                
        #run a simulation of customers buying items in the store for a day
        simulate_day()
        
        #increase the day variable
        

    
def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("StoreName", help="Name of the store")
    parser.add_argument("EmployeeList", help = "Excel file of employees")
    parser.add_argument("StockList", help = "The text file of the stock for the store")
    return parser.parse_args(arglist)    

if __name__ == "__main__":
    args  = parse_args(sys.argv[1:])
    main(args.StoreName, args.EmployeeList, args.StockList)