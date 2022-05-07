import mysql.connector
import database
import pandas as pd

mycursor, commit = database.mysql_connection()


#Query for the number of provoked and unprovoked shark attacks
def provokedUnprovokedAttacks():
    print("Number of Provoked and Unprovoked Attacks")
    provokedUnprovokedAttacks = ("SELECT type, Count(type) AS whichTypeMost FROM shark1 WHERE type IS NOT NULL GROUP BY type ORDER BY whichTypeMost DESC")
    df3 = pd.read_sql(provokedUnprovokedAttacks, mycursor)
    print(df3)
    
    #result.write.csv("results/provokedUnprovokedAttacks")
    #log.write("Executing 'SELECT typeAttack, Count(typeAttack) AS whichTypeMost FROM shark1 GROUP BY typeAttack ORDER BY whichTypeMost';\n")
    import usermenu
