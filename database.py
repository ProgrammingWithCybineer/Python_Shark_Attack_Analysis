import mysql.connector
import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql import HiveContext
import sqlalchemy as sa
import pandas as pd
import database
import mysql.connector
import sys
import os



#connection for login database
def mysql_connection_Login():
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "############################",#### REMOVE BEFORE COMMITING CODE
    database = "Shark_Attack_Login",
    )
    #print(mydb)


    # Create Cursor Instance
    mycursor = mydb.cursor()
    commit = mydb.commit()
    return mycursor, commit







def hive_context():
    
    conf = SparkConf()
    sc = SparkContext.getOrCreate(conf=conf)
    hc = HiveContext(sc)
    return hc, sc, 





def spark_session(): 
    global sc    
    conf = pyspark.SparkConf()\
        .setMaster("local[*]")\
        .setAppName("sharkAnalysis")\
        .setAll([("spark.driver.memory", "1g"),\
        ("spark.executor.memory", "1g")])
        
        
    #spark = SparkSession(sc)\
    spark = SparkSession\
        .builder \
        .master("local[*]") \
        .appName("sharkAnalysis") \
        .config("spark.some.config.option", "some-value")\
        .enableHiveSupport()\
        .getOrCreate()
    spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
        
        
    conf = SparkConf()    
    sc = SparkContext.getOrCreate(conf=conf)
    sqlContext = SQLContext(spark)   
    
    
    return conf, spark, sqlContext, sc, conf
    
    
#connection is for shark database    
def mysql_connection_SharkDatabase():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "############################",#### REMOVE BEFORE COMMITING CODE
        database = "new_shark_attack_test_data",
    )    
    
    #mydb = mysql.connector.connect
    sharkcursor = mydb.cursor()
    sharkcommit = mydb.commit()
    return sharkcursor, sharkcommit, mydb
    

def query_sharkdatabase():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "############################",#### REMOVE BEFORE COMMITING CODE
        database = "Shark_Attack_Login",
    )
    
    
    my_data = pd.read_sql("SELECT * FROM SharkAttackdataTable limit 100", mydb)
    print(my_data)
    
    #sharkcursorquery = mydb.cursor()
    #sharkcursorquery.execute("SELECT * FROM SharkAttackdataTable limit 10")
    #query = ("SELECT * FROM SharkAttackdataTable limit 10")
    #df = pd.read_sql_query(query, mydb)
    #myresult = sharkcursorquery.fetchall()

    

   

class DB:
    # def __del__(self):
        #self.mydb.close()
        

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "############################",#### REMOVE BEFORE COMMITING CODE
            #database = "Shark_Attack_Analysis",
            database = "Shark_Attack_Login",            
        )
        print("Started database connection")
        


    #this will insert into database newly created user
    # def insert_new_user_into_database(self):
        #mycursor = self.mydb.cursor()
        ## NEED TO CREATE SHARKATTACHDATABASE  DATABASE IN MYSQL ######
        #resultSet1 = "INSERT INTO SharkAttackDatabase (userName, userPassword, userPassword2) VALUES (%s, %s, %s)"
        #answer = (userName, userPassword, userPassword2)
        #mycursor.execute(resultSet1,answer)
        #mycursor.commit()
        #userMenu()
        
        #mycursor.close()

    # sharkAttackData()
    def sharkAttackData(self):
        sharkdata = pd.read_csv('input/GSAF5_2000.csv',  keep_default_na=False, index_col=False, delimiter = ',')
        sharkdata.head()
        mycursor = self.mydb.cursor()
        
        if self.mydb.is_connected():
            sharkcursor = self.mydb.cursor() 
            sharkcursor.execute("select database();")
            record = sharkcursor.fetchone()
            
            print("You're connected to database: ", record)
            sharkcursor.execute("DROP TABLE IF EXISTS SharkAttackDataTable;")
            print('Creating table....')
            
            #pass the create table statement which you want to create
            sharkcursor.execute('CREATE TABLE SharkAttackDataTable(caseNumber varchar(255), date varchar(255), year int, typeAttack varchar(255), country varchar(255), area varchar(255), location varchar(255), activity varchar(255), name varchar(255), sex varchar(255), age int, injury varchar(255), fatal varchar(255), time varchar(255), species varchar(255), investigator_or_source varchar(255), pdf varchar(255), href_formula varchar(255), href varchar(255), case_number1 varchar(255), case_number varchar(255), original_order varchar(255))')
            
            print("Table is created....")
                
            #loop through the data frame
            for i,row in sharkdata.iterrows():
                #here %S means string values 
                sql = "INSERT INTO shark_attack_login.SharkAttackdataTable VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                sharkcursor.execute(sql, tuple(row))
                print("Record inserted")
                
                # the connection is not auto committed by default, so we must commit to save our changes
                self.mydb.commit()
        mycursor.close()
        
        
    
    # def do_something_connection(self):
    # def connect_to_mysql(self):
        #mycursor = self.mydb.cursor()
        #mydb = mysql.connector.connect(
        #host = "localhost",
        #user = "root",
        #passwd = "#################",#### REMOVE BEFORE COMMITING CODE
        #database = "Shark_Attack_Login",
        #)
        #print(mydb)


        # Create Cursor Instance
        #mycursor = mydb.cursor()
        #mycursor.close()
        
        
        
        
        


    
        
        
 




