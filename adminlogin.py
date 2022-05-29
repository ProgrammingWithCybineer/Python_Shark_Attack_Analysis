import pandas as pd
import mysql.connector
import sys
import os
from database import DB



#logging in as Admin
def adminLogIn():
    global adminName
    global adminPassword
   
    DB().connectToDatabase()
       
    print("Type Admin UserName")
    adminName = input("> ")
    print("")
    print("Type Admin Password")
    adminPassword = input("> ")
    print("")
    
    DB().logInAsAdmin()
            

adminLogIn()