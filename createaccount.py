import mysql.connector
import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql import HiveContext
import sqlalchemy as sa
import pandas as pd
#import database
import mysql.connector
import sys
import os
from database import DB


#userName = ""
#userPassword = ""
#userPassword2 = ""
       

DB().createAccountConnection()  


#mycursor = mydb.cursor()
#commit = mydb.commit()
def createUserAccount():
    global userName
    global userPassword 
    global userPassword2
      
         
    print("")
    print("Please type your username")
    userName = input("> ")
    print("")
    print("Please type your password")
    userPassword = input("> ")
    print("")
    print("Please type your retype password")
    userPassword2 = input("> ")
    
    
    DB().addUserToDatabase()
    return userName, userPassword, userPassword2    
  


#    if (userPassword == userPassword2):
        
#        print(" Account has been created")
#        print("")
#        resultSet1 = "INSERT INTO SharkAttackDatabase (userName, userPassword, userPassword2) VALUES (%s, %s, %s)"
#        answer = (userName, userPassword, userPassword2)
#        mycursor.execute(resultSet1, answer)
#        mydb.commit()
        
#        import usermenu

#    elif (userPassword != userPassword2):
#        print(" Passwords do not match, please try again")
#        print("")
#       createAccount()


#    elif (userPassword is None):
#        print(" Password Cannot Be Blank")
#        print("")
#        createAccount()
    
        
              
createUserAccount()