import mysql.connector
from queries import typesOfQueries
import pandas as pd
import sys
import os
from usermenu import userQueryMenu


def totalSharkAttacks():
      
    print("Total number of attacks recorded...")
    
     
    
    typesOfQueries().totalnumbersharkattacks()
    
    
    userQueryMenu()


totalSharkAttacks()

