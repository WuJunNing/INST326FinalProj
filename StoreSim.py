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
        inventory = {}
        with open(filename, "r", encoding = "utf-8") as f:
            expr = (r"""(?gm)
                    ^
                    (?:(?P<item>[a-z]+)*\s)
                    (?P<price>\d*)""")
            for line in f:
                stock_item = re.search(expr, line)
                if stock_item:
                    stockname = stock_item.group("item")
                    stockprice = stock_item.group("price")
                    inventory[itemname] = itemprice
                    
    
def run_game(StockFilePath):
    
        """Runs a full simulation game, over a series of 
            game days.
                
            Side effects: Prints the game result to the terminal. 
        """
        #populate inventory with the available stock
        read_stock(StockFilePath)
        
        #continues looping and running the simulation until the player 
        #completes 5 days or runs out of money
        while day < 6:
            #player loses if they run out of money
            if funds == 0:
                print(f'Sorry, you ran out of money after day {day - 1}')
                return
            
            #run one day simulation
            run_day()
        
        #return either a win message or a lose message after 14 days. 
        #we can edit the win condition but for now I put $500 in profit
        if profit >= 500:
            print(f'''Congratulations, you won the game. You made
                  ${profit} in 5 days''')
            return
        else:
            print(f'''Sorry, you lost the game. You only made 
                  {profit} in 5 days.''')
            return
    
def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("StoreName", help="Name of the store")
    parser.add_argument("EmployeeList", help = "Excel file of employees")
    parser.add_argument("StockList", help = "The text file of the stock for the store")
    return parser.parse_args(arglist)    

if __name__ == "__main__":
    args  = parse_args(sys.argv[1:])
    main(args.StoreName, args.EmployeeList, args.StockList)