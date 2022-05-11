from argparse import ArgumentParser
import sys

def main(storeName, EmployeeFilePath):
    print("SSSSSSSSSSSSS")
    print(storeName)
    print(EmployeeFilePath)
    #run the game
    run_game()
    
def run_game():
        """Runs a full simulation game, over a series of 
            game days.
                
            Side effects: Prints the game result to the terminal. 
        """
        #populate inventory with the available stock
        read_stock()
        
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
    return parser.parse_args(arglist)    

if __name__ == "__main__":
    args  = parse_args(sys.argv[1:])
    main(args.StoreName, args.EmployeeList)