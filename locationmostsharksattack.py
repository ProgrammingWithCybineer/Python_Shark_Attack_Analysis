import mysql.connector
import database
import pandas as pd

mycursor, commit = database.mysql_connection()


# Query for location of most shark attacks
def locationMostSharksAttacks():
    print("Location of Most Shark Attack...")
    locationMostSharksAttacks = "SELECT (country) FROM shark1 WHERE country IS NOT NULL GROUP BY country ORDER BY COUNT(*) DESC"
    df1 = pd.read_sql(locationMostSharksAttacks, mycursor)
    print(df1)
    
    #result.write.csv("results/locationMostSharksAttacks")
    #log.write("Executing 'SELECT (country) FROM shark1 WHERE country IS NOT NULL GROUP BY country ORDER BY COUNT(*) DESC';\n")
    
    import usermenu
    
    



locationMostSharksAttacks()