import mysql.connector
import sqlalchemy
import database
import pandas as pd
import csv


mycursor, commit = database.mysql_connection()



#Query for location of most shark attacks
def locationMostSharksAttacks():
    print("Location of Most Shark Attack...")
    locationMostSharksAttacks = pd.read_csv("input\GSAF5.csv")
    locationMostSharksAttacks.query = "SELECT (country) FROM GSAF5 WHERE country IS NOT NULL GROUP BY country ORDER BY COUNT(*) DESC"
    # df1 = pd.read_sql(locationMostSharksAttacks, mycursor)
    print(locationMostSharksAttacks)
    #locationMostSharksAttacks.head()
    

    
    #result.write.csv("results/locationMostSharksAttacks")
    #log.write("Executing 'SELECT (country) FROM shark1 WHERE country IS NOT NULL GROUP BY country ORDER BY COUNT(*) DESC';\n")
    #import usermenu
 
    import usermenu

locationMostSharksAttacks()