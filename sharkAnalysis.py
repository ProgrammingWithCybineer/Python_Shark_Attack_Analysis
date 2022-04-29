import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import HiveContext
import mysql.connector

userName = ""


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
        



#Create User Account    
def createAccount():
    global userName
    print("Please type your username")
    userName = input("> ")
    print("")
    print("Please type your password")
    userPassword = input("> ")
    print("")
    print("Please type your retype password")
    userPassword2 = input("> ")
    if (userPassword == userPassword2):
        print(" Account has been created")
        print("")
        userMenu()

    elif (userPassword != userPassword2):
        print(" Passwords do not match, please try again")
        print("")
        print("Please type your password!!")
        userPassword = input("> ")
        print("")
        print("Please type your retype password!!")
        userPassword2 = input("> ")
        print(" Account has been created!!!")
        print("")
        userMenu()

    elif (userPassword == ""):
        print(" Password Cannot Be Blank")
        print("")
        print("Please type your password!!")
        userPassword = input("> ")
        print("")
        print("Please type your retype password!!")
        userPassword2 = input("> ")
        print(" Account has been created!!!")
        print("")
        userMenu()
    
    #Updating table with userName and password after creating a new account
    #val resultSet2 = statement.executeUpdate("INSERT INTO userAccount (userName, userPassword, userPassword2) VALUES ('"+userName+"', '"+userPassword+"',  '"+userPassword2+"');")
    #log.write("Executing 'INSERT INTO userAccount (userName, userPassword, userPassword2) VALUES ('"+userName+"', '"+userPassword+"',  '"+userPassword2+"');\n")


#User logging in
def userLogIn():
    print(" Please type a User Name")
    userName = input("> ")
    print("")
    print(" Please type A Password")
    userPassword = input("> ")
    resultSet = statement.executeQuery("SELECT COUNT(*) FROM userAccount WHERE userName='"+userName+"' AND userPassword='"+userPassword+"';")
    #log.write("Executing 'SELECT COUNT(*) FROM userAccount WHERE userName='"+userName+"' AND userPassword='"+userPassword+"');\n")
    while ( resultSet.next()):
        if (resultSet.getString(1) == "1"):
            print("You Have Logged In Successfully")
            userChoice()
            
        else:
            print("Username/password combo not found. Try again!")
            userLogIn()


   
#option for user to choose query menu or user data menu
def userChoice():
    print(" Welcome User. Please choose from below: ")
    print("################################")
    print(" (1) User Query menu")
    print("")
    print(" (2) User Information Menu")
    print("")
    print(" (3) Main menu")
    print("")
    print(" (4) Exit the program")
    print("####################################")
    choice2 =  input(int("> "))
    
    if (choice2 == 1):
        print(" User Query Menu...")
        userMenu()

        
    elif (choice2 == 2): 
        print(" User Information Menu")
        userInformationOption()
        
    elif (choice2 == 3): 
        print(" Main Menu")
        mainMenu()
        
    elif (choice2 == 4): 
        print(" Exit Program")
        exitProgram()
        
        
    elif ((choice2 != 1 or choice2 != 2 or choice2 != 3 or choice2 != 4)): 
        print(" Not a valid choice, please try again!!!")
        userChoice()
        


def userInformationOption():
    global userName
    global userNameUpdate
    global userPasswordUpdate
    global userPasswordUpdate2
    print("")
    print("################################")
    print(" (1) Update User Name ")
    print("")
    print(" (2) Update User Password")
    print("")
    print(" (3) Previous Menu ")
    print("")
    print(" (0) Exit the program ")
    print("")
    print("#################################")
    choice2 =  input(int("> "))
    
    if (choice2 == 1):
        print(" Type A New User Name")
        userNameUpdate = input("> ")
        #resultSet2_1 = statement.executeUpdate("UPDATE userAccount SET userName = ('"+userNameUpdate+"') WHERE userName = ('"+userName+"');")
        #log.write("UPDATE userAccount SET userName = ('"+userNameUpdate+"') WHERE username = ('"+userName+"') \n")
        print("User Name Updated")
        userChoice()

    elif (choice2 == 2):
        print("Type User Name")
        userName = input("> ")
        print(" Type A New Password")
        userPasswordUpdate = input("> ")
        #resultSet2_2 = statement.executeUpdate("UPDATE userAccount SET userPassword = ('"+userPasswordUpdate+"') WHERE userName = ('"+userName+"');")
        #log.write("UPDATE userAccount SET userPassword = ('"+userPasswordUpdate+"') WHERE username = ('"+userName+"') \n")
        print(" ReType Password")
        userPasswordUpdate2 = input("> ")
        #resultSet2_3 = statement.executeUpdate("UPDATE userAccount SET userPassword2 = ('"+userPasswordUpdate2+"') WHERE userName = ('"+userName+"');")
        #log.write("UPDATE userAccount SET userPassword2 = ('"+userPasswordUpdate2+"') WHERE username = ('"+userName+"') \n")
        print("User Name Updated")
        userChoice()

    elif (choice2 == 3):
        userChoice()

    elif (choice2 == 0):
        exitProgram()
    
    elif (( choice2 != 0 or choice2 != 1 or choice2 != 2 or choice2 != 3)): 
        print(" Not a valid choice, please try again!!!")
        userChoice()
    



# User Menu
def userMenu():
    #sharkAttackData()
    print(" What type of data would you like to view. Please select below: ")
    print("")
    print(" (1) What is the total number of shark attacks recorded?")
    print("")
    print(" (2) What shark is responsible for the most shark attacks?")
    print("")
    print(" (3) Where do the most shark attacks happen?")
    print("")
    print(" (4) What time of day do most shark attacks happen?")
    print("")
    print(" (5) Are most shark attacks provoked or unprovoked?")
    print("")
    print(" (6) What is the age range of people attacked by sharks?")
    print("")
    print(" (7) Return to Main Menu")
    print("")
    print(" (0) To exit the program")
    print("")
    choice3 =  input(int("> "))
     
    if (choice3 == 1):
        print(" What is the total number of shark attacks recorded?")
        totalSharkAttacks()
        userMenu()

        
    elif (choice3 == 2):
        print(" What shark is responsible for the most shark attacks?")
        sharkResponsible()
        userMenu()
        
    elif (choice3 == 3):
        print(" Where do the most shark attacks happen?")
        locationMostSharkAttacks()
        userMenu()
        
    elif (choice3 == 4): 
        print(" What time of day do most shark attacks happen?")
        timeOfDaySharkAttack()
        userMenu()
        
    elif (choice3 == 5):
        print(" Are most shark attacks provoked or unprovoked?")
        provokedUnprovokedAttacks()
        userMenu()
        
    elif (choice3 == 6): 
        print(" What is the age range of people attacked by sharks?")
        ageRangePeopleAttacked()
        userMenu()
    

    elif (choice3 == 7):
        print(" Return To Log In Screen...")
        mainMenu()

    elif (choice3 == 0):
        exitProgram()
        
    elif (( choice3 != 0 or choice3 != 1 or choice3 != 2 or choice3 != 3 or choice3 != 4 or choice3 != 5 or choice3 != 6 or choice3 != 7)):
        print(" Not a valid choice, please try again!!!")
        userMenu()
        
    




#logging in as Admin
def adminLogIn():
    #val statement2 = connection.createStatement()
    print("Type Admin UserName")
    userAdmin = input("> ")
    print("")
    print("Type Admin Password")
    adminPassword = input("> ")
    print("")     
    resultSet2 = statement.executeQuery("SELECT COUNT(*) FROM adminAccount WHERE userAdmin='"+userAdmin+"' AND adminPassword='"+adminPassword+"';")
    #log.write("Executing 'SELECT COUNT(*) FROM adminAccount WHERE userAdmin='"+userAdmin+"' AND adminPassword='"+adminPassword+"');\n")
    while ( resultSet2.next() ): 
        if (resultSet2.getString(1) == "1"):
            print(" Log In Successful!!")
            adminMenu()
        else:
            print("Username/password combo not found. Try again!")
            print("")
            adminLogIn()
                                
               


#Admin menu options
def adminMenu():
    print("")
    print(" Welcome Admin. Please choose from below: ")
    print("################################")
    print(" (1) Update dataset ")
    print("")
    print(" (2) Delete a User from the Database")
    print("")
    print(" (3) Exit the program")
    print("####################################")
    choice4 =  input(int("> "))
    
    if (choice4 == 1):
        print(" choice 1")
        updateDataset()                            
    
    elif (choice4 == 2) :
        print(" choice 2.")
        deleteUser()
    
    elif (choice4 == 3): 
        print(" choice 3.")
        exitProgram()
    
    elif (( choice4 != 1 or choice4 != 2 or choice4 != 3)):
        print(" Not a valid choice, please try again!!!")
        adminMenu()
    
    


#Update the data for user options 
def updateDataset():
    print("")
    print(" Please choose from below ")
    print("############################")
    print(" (1) Update Data")
    print("")
    print(" (2) Return to Admin Menu ")
    print("")
    print(" (3) Exit program ")
    print("#############################")
    print("")
    
    choice3 = input(int("> "))
     
    if (choice3 == 1):
        print(" Updating Data on file ....")
        sharkAttackData()                          
    
    elif (choice3 == 2):
        adminMenu()
    
    elif (choice3 == 3): 
        print("Exiting Program.....")
        exitProgram()

    elif (( choice3 != 1 or choice3 != 2 or choice3 !=3 )):
        print(" Not a valid choice, please try again!!!")
        adminMenu()
    



#DELETE USER 
def deleteUser():
    print("")
    print("################################")
    print(" (1) Choose A User To Delete ")
    print("")
    print(" (2) Exit the program")
    print("")
    print("#################################")
    choice2 = input(int("> "))
     
    if (choice2 == 1):
        #resultSet4 = statement.executeQuery("SELECT * FROM userAccount")
        #log.write("Executing 'SELECT * FROM userAccount';\n")
        print(" Type A User's Name")
        userName =  scanner.nextLine().trim()
        #resultSet3 =  statement.executeUpdate("DELETE FROM userAccount WHERE userName = ('"+userName+"');")
        #log.write("Executing 'DELETE User from database' \n")
        print("User Deleted")
        #resultSet5 = statement.executeQuery("SELECT * FROM userAccount")
        #log.write("Executing 'SELECT * FROM userAccount';\n")
        adminMenu()

    elif (choice2 == 2):
        print(" choice 2.")
        exitProgram()
    
    elif (( choice2 != 1 or choice2 != 2 )):
        print(" Not a valid choice, please try again!!!")
        deleteUser()
    


#Exit program
def exitProgram():
    print("")
    print("                                                                                                         ")
    print("                                  *                                                                      ") 
    print("                                *   *                                                                    ")
    print("                               *     *                                   *                               ")
    print("                              *       *                                 * *                              ")
    print("                             *         *                               *   *                             ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~*~~~~~~~~~~~*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*~~~~~*~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                             THANK YOU FOR VISITING THE SHARK ATTACK DATABASE                            ")
    print("                                       DO STAY SAFE IN THEIR OCEANS                                      ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")        
    print("")
    print("")
shark = False
    
















        
mainMenu()


