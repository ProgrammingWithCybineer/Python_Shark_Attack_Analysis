import mysql.connector
import database
import pandas as pd


mycursor, commit = database.mysql_connection()



#Query for what shark is responsible for the most attacks
def sharkResponsible():
    print("What Shark is responsible for the most attacks...")
    sharkResponsible = pd.read_csv("input\GSAF5.csv")
    sharkResponsible.query = "SELECT (species) FROM GSAF5 WHERE species IS NOT NULL GROUP BY species ORDER BY COUNT(*) DESC"
    #sharkResponsible.head()
    print(sharkResponsible)
    
    
    
    #This will write results of query to new csv file    
    #sharkResponsible.write.csv("results/sharkResponsible")
    
    
    #log.write("Executing 'SELECT (species) FROM shark1 GROUP BY species ORDER BY COUNT(*) DESC';\n")
    
    
    import usermenu

sharkResponsible()

