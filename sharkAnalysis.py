import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import HiveContext
import pandas as pd

import sys
import os



#output = ""
conf = SparkConf()
sc = SparkContext.getOrCreate(conf=conf)


Conf = pyspark.SparkConf()\
    .setMaster("local[*]")\
    .setAppName("sharkAnalysis")\
    .setAll([("spark.driver.memory", "40g"),\
    ("spark.executor.memory", "50g")])
    
    
    
spark = SparkSession(sc)\
        .builder \
        .master("local[*]") \
        .appName("sharkAnalysis") \
        .config("spark.some.config.option", "some-value")\
        .enableHiveSupport()\
        .getOrCreate()
        
          

#sc = SparkContext(spark)
#hiveCtx = HiveContext(spark)
#hiveCtx = SparkSession.withHiveSupport(spark)
sqlContext = SQLContext(spark)  
#output = hiveCtx.read

#print(sc)

    
#Start of program
def mainMenu():
    print("###################################")
    print("Please choose from a Number the menu below: ")
    print("(1) Create Account ")
    print("(2) User Log In ")
    print("(3) Admin Log In ")
    print("(0) Quit Program")
    print("###################################")
    choice = int(input("> "))
    
    if (choice == 1):
        #createAccount()
        import createaccount
        #print("1")
            
    elif(choice == 2):
        #userLogIn()
        import userlogin
        #print("2")

    elif(choice == 3):
        #adminLogIn()
        import adminlogin
        #print("3")

    elif(choice == 0):
        #exitProgram()
        import exitprogram
        #print("0")
            
    elif(( choice != 0 or choice != 1 or choice != 1 or choice or 2 or choice != 3 )):
        print("Not a valid choice. Try again")
        mainMenu()
        
mainMenu()


