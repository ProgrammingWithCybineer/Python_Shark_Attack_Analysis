import mysql.connector
import database
import pandas as pd

mycursor, commit = database.mysql_connection()


#Query for the number of provoked and unprovoked shark attacks
def provokedUnprovokedAttacks():
    print("Number of Provoked and Unprovoked Attacks")
    provokedUnprovokedAttacks = pd.read_csv("input\GSAF5.csv")
    provokedUnprovokedAttacks.query = "SELECT type, Count(type) AS whichTypeMost FROM GSAF5 WHERE type IS NOT NULL GROUP BY type ORDER BY whichTypeMost DESC"
    
    print(provokedUnprovokedAttacks)
    
    
    #This will write results of query to new csv file    
    #provokedUnprovokedAttacks.write.csv("results/provokedUnprovokedAttacks")
    
  
    #log.write("Executing 'SELECT typeAttack, Count(typeAttack) AS whichTypeMost FROM shark1 GROUP BY typeAttack ORDER BY whichTypeMost';\n")
    import usermenu


provokedUnprovokedAttacks()