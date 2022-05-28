import mysql.connector
import sqlalchemy
import database
from database import DB
import pandas as pd
import csv

#mycursor, commit = database.mysql_connection_Login()

def totalSharkAttacks():
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "##################", #### REMOVE BEFORE COMMITTING CODE
    database = "Shark_Attack_Login",
    )
    print("You're Connected. You can now run your query")
    
    print("Total number of attacks recorded...")
    totalSharkAttacks = "SELECT COUNT(year) AS TotalAttacks FROM SharkAttackDataTable WHERE year > 1950"
    mycursor = mydb.cursor()        
    mycursor.execute(totalSharkAttacks)
    output = mycursor.fetchall()
    for x in output:
        print(x)    
    #This will write results of query to new csv file    
    #totalSharkAttacks.write.csv("results/totalSharkAttacks")
    
    #log.write("Executing 'SELECT COUNT(year) FROM shark1 WHERE year > 1950';\n")
   
    import usermenu

totalSharkAttacks()

