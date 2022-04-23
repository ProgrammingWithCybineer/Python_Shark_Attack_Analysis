import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import HiveContext
import mysql.connector



#output = ""

Conf = pyspark.SparkConf()\
    .setMaster("local")\
    .setAppName("sharkAnaysis")\
    .setAll([("spark.driver.memory", "40g"),\
    ("spark.executor.memory", "50g")])

sc = SparkContext(Conf)
hiveCtx = HiveContext(sc)
output = hiveCtx.read

#print(sc)

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "#########################",#### REMOVE BEFORE COMMITING CODE
database = "Shark_Attack_Login",
)

# Create Cursor Instance
my_cursor = mydb.cursor()


def sharkAttackData():
    output = hiveCtx.read\
    .format("csv")\
    .option("inferSchema", "true")\
    .option("header", "true")\
    .load("input/GSAF5 (1_2).csv")
            
    #output.limit(20).show() // will print out the first 20 lines
    #This code will create a temp view of the dataset you used and load the data into a permanent table
    #inside of Hadoop. this will persist the data and only require this code to run once.
    #After initialization this code will and creation of output will not me necessary
    output.createOrReplaceTempView("temp_data")
    hiveCtx.sql("SET hive.exec.dynamic.partition.mode=nonstrict")
    hiveCtx.sql("SET hive.enforce.bucketing=false")
    hiveCtx.sql("SET hive.enforce.sorting=false")
    #hiveCtx.sql("USE project1_hive_scala")
    hiveCtx.sql("CREATE TABLE IF NOT EXISTS shark1 (caseNumber STRING, date STRING, year INT, type STRING, country STRING, area STRING, location STRING, activity STRING, name STRING, sex STRING, age INT, injury STRING, fatal STRING, time STRING, species STRING, investigator_or_source STRING, pdf STRING, href_formula STRING, href_ STRING, case_number1 STRING, case_number STRING, original_order INT)")
    hiveCtx.sql("INSERT INTO shark1 SELECT * FROM temp_data")
    sharkTable = hiveCtx.sql("SELECT * FROM shark1 limit 10")
    sharkTable.show()
    
    
    
#Start of program
def mainMenu():
    print("###################################")
    print("Please choose from a Number the menu below: ")
    print("(1) Create Account ")
    print("(2) User Log In ")
    print("(3) Admin Log In ")
    print("(0) Quit Program")
    print("###################################")
    choice = input(int("> "))
      

    if (choice == 1):
        #createAccount()
        print("1")
            
    elif(choice == 2):
        #userLogIn()
        print("2")

    elif(choice == 3):
        #adminLogIn()
        print("3")

    elif(choice == 0):
        #exitProgram()
        print("0")
            
    elif(( choice != 0 or choice != 1 or choice != 1 or choice or 2 or choice != 3 )):
        print("Not a valid choice. Try again")
        mainMenu()
        
        
mainMenu()


