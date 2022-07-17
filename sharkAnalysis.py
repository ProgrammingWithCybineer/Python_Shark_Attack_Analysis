import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
import sqlalchemy as sa
import pandas as pd
from database import DB
import mysql.connector
import os



    
#Start of program
def mainMenu():
    print("")
    print("                                                                                                         ")
    print("                                  *                                                                      ") 
    print("                                *   *                                                                    ")
    print("                               *     *                                   *                               ")
    print("                              *       *                                 * *                              ")
    print("                             *         *                               *   *                             ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~*~~~~~~~~~~~*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*~~~~~*~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                             WELCOME TO THE SHARK ATTACK ANALYSIS DATABASE                               ")
    print("                                                                                                         ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
    print("")
    print("###################################")
    print("Please choose from a Number the menu below:")
    print("(1) Create User Account")
    print("(2) User Log In ")
    print("(3) Admin Log In ")
    print("(0) Quit Program")
    print("###################################")
    choice = int(input("> "))
    
    if (choice == 1):
        import createaccount
            
    elif(choice == 2):
        import userlogin
        

    elif(choice == 3):
        import adminlogin
        

    elif(choice == 0):
        import exitprogram
        
            
    elif(( choice != 0 or choice != 1 or choice != 1 or choice or 2 or choice != 3 )):
        print("Not a valid choice. Try again")
        mainMenu()
        
mainMenu()


