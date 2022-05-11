from argparse import ArgumentParser
from mancala import parse_args


def main(storeName, EmployeeFilePath):
    print(storeName)
    print(EmployeeFilePath)
    
def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("StoreName", help="Name of the store")
    parser.add_argument("EmployeeList", help = "Excel file of employees")
    return parser.parse_args(arglist)    

if __name__ == "main":
    args  = parse_args(sys.argv[1:])
    main(args.StoreName, args.EmployeeList)