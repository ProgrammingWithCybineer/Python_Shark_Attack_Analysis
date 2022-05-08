import mysql.connector
import sqlalchemy
import database
import pandas as pd
import csv

mycursor, commit = database.mysql_connection()

    
# Query for total number of shark attacks since certain date
def totalSharkAttacks():
    print("Total number of attacks recorded...")
    totalSharkAttacks = pd.read_csv("input\GSAF5.csv")
    totalSharkAttacks.query = "SELECT COUNT(year) AS TotalAttacks FROM GSAF5 WHERE year > 1950"
    print(totalSharkAttacks)
    
    
    #This will write results of query to new csv file    
    #totalSharkAttacks.write.csv("results/totalSharkAttacks")
    
    #log.write("Executing 'SELECT COUNT(year) FROM shark1 WHERE year > 1950';\n")
   
    import usermenu

totalSharkAttacks()

