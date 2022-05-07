import mysql.connector
import database
import pandas as pd

mycursor, commit = database.mysql_connection()




#Query for what shark is responsible for the most attacks
def sharkResponsible():
    print("What Shark is responsible for the most attacks...")
    sharkResponsible = "SELECT (species) FROM shark1 WHERE species IS NOT NULL GROUP BY species ORDER BY COUNT(*) DESC"
    df4 = pd.read_sql(sharkResponsible, mycursor)
    print(df4)
     
    
    #log.write("Executing 'SELECT (species) FROM shark1 GROUP BY species ORDER BY COUNT(*) DESC';\n")
    
    
    import usermenu

sharkResponsible()

