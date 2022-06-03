import pandas as pd
import mysql.connector
import sys
import os
from database import DB



#logging in as Admin
def adminLogIn():
    DB().connectToDatabase()
    global adminName
    global adminPassword 
      
    print("Type Admin UserName")
    adminName = input("> ")
    print("")
    print("Type Admin Password")
    adminPassword = input("> ")
    print("")
    
    DB().logInAsAdmin()
            

adminLogIn()