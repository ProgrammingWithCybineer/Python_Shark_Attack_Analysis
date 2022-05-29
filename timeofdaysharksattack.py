import mysql.connector
import sqlalchemy
import database
import pandas as pd
import csv
   
mycursor, commit = database.mysql_connection()

   
#STILL NEED TO FIGURE OUT THIS QUERY
# Query for what time of day do most shark attacks occur
def timeOfDaySharkAttack():
    print("Time most shark attacks occur...")
    timeOfDaySharkAttack1 = pd.read_csv("input\GSAF51.csv")
    timeOfDaySharkAttack1.query = "CREATE VIEW IF NOT EXISTS GSAF51 AS SELECT CAST(regexp_replace(time, 'h00', '') AS int) AS time FROM GSAF5 WHERE time IS NOT NULL LIMIT 10"
    timeOfDaySharkAttack1.query = "SELECT AVG(time) FROM GSAF51 WHERE time IS NOT NULL"
    
    #Date Cleanup: Date and Time
    #pd.to_datetime(timeOfDaySharkAttack1).iloc[:100]
    #pd.to_datetime(timeOfDaySharkAttack1).dt.strftime("%Y-%m-%d %H:%M:S")
    #timeOfDaySharkAttack1.head()
    print(timeOfDaySharkAttack1)
    
    #This will write results of query to new csv file    
    #timeOfDaySharkAttack.write.csv("results/timeOfDaySharkAttack")
    
    
    #log.write("Executing 'NEED TO ADD LOG HERE');\n")
    
    import usermenu


timeOfDaySharkAttack()