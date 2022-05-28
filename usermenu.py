import mysql.connector
from mysql.connector import Error
import database
import pandas as pd
import numpy as np
import sys
import os
from database import DB


# User Menu
def userMenu():
                   
        print("")
        print(" What type of data would you like to view. Please select below: ")
        print("")
        print(" (1) What is the total number of shark attacks recorded?")
        print("")
        print(" (2) What shark is responsible for the most shark attacks?")
        print("")
        print(" (3) Where do the most shark attacks happen?")
        print("")
        print(" (4) What time of day do most shark attacks happen?")
        print("")
        print(" (5) Are most shark attacks provoked or unprovoked?")
        print("")
        print(" (6) What is the age range of people attacked by sharks?")
        print("")
        print(" (7) Return to Main Menu")
        print("")
        print(" (0) To exit the program")
        print("")
        
        choice3 = int(input("> "))
        
        if (choice3 == 1):
            print(" What is the total number of shark attacks recorded?")
            import totalsharkattacks
            
            
        elif (choice3 == 2):
            print(" What shark is responsible for the most shark attacks?")
            import sharkresponsible
        
            
        elif (choice3 == 3):
            print(" Where do the most shark attacks happen?")
            import locationmostsharksattack
        
            
        elif (choice3 == 4): 
            print(" What time of day do most shark attacks happen?")
            import timeofdaysharksattack
            
            
        elif (choice3 == 5):
            print(" Are most shark attacks provoked or unprovoked?")
            import provokedunprovokedattacks
            
            
        elif (choice3 == 6): 
            print(" What is the age range of people attacked by sharks?")
            import agerangepeopleattacked
            
        

        elif (choice3 == 7):
            print(" Return To Log In Screen...")
            import sharkAnalysis

        elif (choice3 == 0):
            import exitprogram
            
        elif (( choice3 != 0 or choice3 != 1 or choice3 != 2 or choice3 != 3 or choice3 != 4 or choice3 != 5 or choice3 != 6 or choice3 != 7)):
            print(" Not a valid choice, please try again!!!")
            userMenu()
            
        else:
            #import sharkattackdata
            import sharkattackdata
        
userMenu()