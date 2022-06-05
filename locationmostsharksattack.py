import mysql.connector
from queries import typesOfQueries
import pandas as pd


#Query for location of most shark attacks
def locationMostSharksAttacks():
    
    print("Location of Most Shark Attack...")
    
    typesOfQueries().locationSharkAttacksHappen()
    
 
    

locationMostSharksAttacks()