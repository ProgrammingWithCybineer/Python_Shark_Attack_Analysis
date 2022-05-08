import mysql.connector
import database
import pandas as pd
import numpy as np

hc, sc = database.hive_context()
#conf, spark, sqlContext, sc, conf = database.spark_session()  




def sharkAttackData():
    
    hc = pd.read_csv("input/GSAF5.csv") 
    #output = pd.read.csv\
    #.format("csv")\
    #.option("inferSchema", "true")\
    #.option("header", "true")\
    #.load("input/GSAF5 (1_2).csv")
    
                
    #output.limit(20).show() // will print out the first 20 lines
    #This code will create a temp view of the dataset you used and load the data into a permanent table
    #inside of Hadoop. this will persist the data and only require this code to run once.
    #After initialization this code will and creation of output will not me necessary
    hc.createOrReplaceTempView("temp_data")
    hc.sql("SET hive.exec.dynamic.partition.mode=nonstrict")
    hc.sql("SET hive.enforce.bucketing=false")
    hc.sql("SET hive.enforce.sorting=false")
    
    hc.sql("CREATE TABLE IF NOT EXISTS shark1 (caseNumber STRING, date STRING, year INT, type STRING, country STRING, area STRING, location STRING, activity STRING, name STRING, sex STRING, age INT, injury STRING, fatal STRING, time STRING, species STRING, investigator_or_source STRING, pdf STRING, href_formula STRING, href_ STRING, case_number1 STRING, case_number STRING, original_order INT)")
    hc.sql("INSERT INTO shark1 SELECT * FROM temp_data")
    sharkTable = hc.sql("SELECT * FROM shark1 limit 10")
    sharkTable.show()
    
    
sharkAttackData()
    

