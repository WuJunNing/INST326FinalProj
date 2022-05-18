## Functionality of files in the repository<br>
storestock.txt contains all the items for the store, and their prices. This file will be read by the program to fill the inventory of the store and prices will be used to calculate the profits.<br>
StoreSim.py is the main program, and will run the store simulation. The store will be managed and simulated using this file.<br>
employeenames.txt contains a list of names of the employees to be read by the program. This will be read by the program to get employees for the store.<br>

## Running the program from the command line<br>
Enter the following into the command line:<br>
`StoreSim.py employeenames.txt storestock.txt`<br>
These files, in order, are the main program, the list of employees, and the store's stock.<br>

## Using the program and interpreting output <br>
For each day simulated, follow the prompts printed to manage the employees and keep your store afloat.<br>
At the end of the simulation, you will either win or lose, depending on how high a profit made.<br>
At the end of the simulation, you will be the option between 2 different graphs to display. One will be funds over time, and the other will be profit over time.<br>

## Attributions
Luis: graphFilter() and graphGenerator() functions. pandas and data visualization.<br>
Simon: Employee class and its methods. optional parameters/keyword arguments and conditional expressions.<br>
Ogenna: run_game() and run_day() functions. f-strings and sequence unpacking.<br>
Yabing: read_stock() and simulate_day() functions. regular expressions and with statements.<br>

## Citations
"Warnings - Warning Control" Python 3.10.4 Documentation
Usage: Program relies on using Pandas.append() Method in order to operate the dataframes used for graphing, this module silences all FutureWarning warnings prompted by the program. 
