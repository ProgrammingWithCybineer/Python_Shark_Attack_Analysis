import mysql.connector
from queries import typesOfQueries
import pandas as pd
import sys
import os

from usermenu import *



#Query for what shark is responsible for the most attacks
def sharkResponsible():
    
    typesOfQueries().sharkResponsibleMostAttack()
        
    #This will write results of query to new csv file    
    #sharkResponsible.write.csv("results/sharkResponsible")
    
    
    #log.write("Executing 'SELECT (species) FROM shark1 GROUP BY species ORDER BY COUNT(*) DESC';\n")
    
    
    #import usermenu

sharkResponsible()

