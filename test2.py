import mysql.connector
from mysql.connector import Error
#import mysql.connector
import sys
import os

import pandas as pd

sharkdata = pd.read_csv('input/GSAF51.csv', keep_default_na=False, index_col=False, delimiter = ',')
sharkdata.head()

#To see if try/catch block was needed here
try:
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "############################",#### REMOVE BEFORE COMMITING CODE
    database = "new_shark_attack_test_data",
    )
    
    if mydb.is_connected():
        cursor = mydb.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        
        print("You're connected to database: ", record)
        cursor.execute("DROP TABLE IF EXISTS SharkAttackTable;")
        print('Creating table....')
        
        #pass the create table statement which you want to create
        cursor.execute('CREATE TABLE SharkAttackTable(caseNumber varchar(255), date varchar(255), year varchar(255), typeAttack varchar(255), country varchar(255), area varchar(255), location varchar(255), activity varchar(255), name varchar(255), sex varchar(255), age varchar(255), injury varchar(255), fatal varchar(255), time varchar(255), species varchar(255), investigator_or_source varchar(255), pdf varchar(255), href_formula varchar(255), href varchar(255), case_number1 varchar(255), case_number varchar(255), original_order varchar(255))')
        
        print("Table is created....")
        
             
        
        #loop through the data frame
        for i,row in sharkdata.iterrows():
            #here %S means string values 
            sql = "INSERT INTO new_shark_attack_test_data.SharkAttackTable VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            
            # the connection is not auto committed by default, so we must commit to save our changes
            mydb.commit()
            
except Error as e:
            print("Error while connecting to MySQL", e)