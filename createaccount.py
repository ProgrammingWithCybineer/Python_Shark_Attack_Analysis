import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql import HiveContext
import pandas as pd
import mysql.connector
import sys
import os
from database import DB


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
        
    
    
    
    DB().connectToDatabase()  
    DB().addUserToDatabase()

        
              
createUserAccount()
