import mysql.connector
from queries import typesOfQueries
import pandas as pd
import sys
import os
from usermenu import userQueryMenu
  

   
#STILL NEED TO FIGURE OUT THIS QUERY
# Query for what time of day do most shark attacks occur
def timeOfDaySharkAttack():
    print("Time most shark attacks occur...")
    
    typesOfQueries().timeMostSharkAttacksHappen()
    
    #Date Cleanup: Date and Time
    #pd.to_datetime(timeOfDaySharkAttack1).iloc[:100]
    #pd.to_datetime(timeOfDaySharkAttack1).dt.strftime("%Y-%m-%d %H:%M:S")
    #timeOfDaySharkAttack1.head()
    
    
    #This will write results of query to new csv file    
    #timeOfDaySharkAttack.write.csv("results/timeOfDaySharkAttack")
    
    
    #log.write("Executing 'NEED TO ADD LOG HERE');\n")
    
    userQueryMenu()


timeOfDaySharkAttack()