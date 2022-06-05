import mysql.connector
import database
import pandas as pd
from queries import typesOfQueries



#Query for the number of provoked and unprovoked shark attacks
def provokedUnprovokedAttacks():
    print("Number of Provoked and Unprovoked Attacks")
    
    typesOfQueries().unprovokedVsProvokedAttacks()
    
    
    #This will write results of query to new csv file    
    #provokedUnprovokedAttacks.write.csv("results/provokedUnprovokedAttacks")
    
  
    #log.write("Executing 'SELECT typeAttack, Count(typeAttack) AS whichTypeMost FROM shark1 GROUP BY typeAttack ORDER BY whichTypeMost';\n")
    


provokedUnprovokedAttacks()