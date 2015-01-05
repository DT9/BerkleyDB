import sys
from CreateDatabase import *
from Query1 import *
from Query2 import *
from Query3 import *
from Destroy import *
import os

def createpath(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def main():
    valid = False
    buff = sys.argv[1]
    
    print(buff)
    assert(buff == '1' or buff == '2' or buff == '3')
    
    print("\n\t\t\tWelcome to the Database! ")
    while (True):
        print('') # for that newline organization
        print(" Please type in the number corresponding to the option you wish to select:")
        print(" (1) - Create and populate a database.")
        print(" (2) - Retrieve records with a given key.")
        print(" (3) - Retrieve records with a given value. ")
        print(" (4) - Retrieve records with a given range of key values. ")
        print(" (5) - Destroy the database. ")
        print(" (6) - Quit")
        choice = input(" Please enter your selection: ")
        valid = verifyInput(choice)
        if (valid):
            functionCaller([choice, buff])
        if (choice == "6"):
            break
        
    
def verifyInput(choice):
    if (choice == '1' or choice == '2' or choice == '3'
        or choice == '4' or choice == '6'):
        return True
    
    elif (choice == '5'):  #verify they want to delete database
        yesno = input("Verify that you would like to destroy the database (Y/N): ")
        if (yesno == 'y' or yesno == 'Y'):
            return True
        else:
            
            return False    
        
    else:
        print('')
        print("#######################")
        print(" Error: Invalid input.")
        print("#######################")
        
def functionCaller(arg):
    if (arg[0] == '1'):
        # Call - Create and populate a database.
        CreateDatabase(arg[1])
        
    elif (arg[0] == '2'):
        # Call - Retrieve records with givan key.
        Query1(arg[1])
        
    elif (arg[0] == '3'):
        # Call - Retrieve records with givan data
        Query2(arg[1])

    elif (arg[0] == '4'):
        # Call - Retrieve records with a given range of key values. 
        Query3(arg[1])

    elif (arg[0] == '5'):
        # Call - Destroy the database.
        Destroy(arg[1])
                
    else: #by deafult - nothing else left cause of that there error checking
        #Quit
        Destroy(arg[1])
        try:
            os.remove("answers")
        except:
            pass
        try:
            os.remove("data")
        except:
            pass        
        
        # Probably just  return? It'll exit the program that way
        # Might not even need this else, just leave it and return normal



main()
