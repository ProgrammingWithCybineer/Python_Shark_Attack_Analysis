import mysql.connector
from database import DB



mydb = mysql.connector.connect(
host = "localhost",
user = "root",
passwd = "######################",#### REMOVE BEFORE COMMITING CODE
database = "Shark_Attack_Login",
)
#print(mydb)


# Create Cursor Instance
my_cursor = mydb.cursor()


#Create User Account    
def createAccount():    
    #global userName
    print("")
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
        ## NEED TO CREATE SHARKATTACHDATABASE  DATABASE IN MYSQL ######
        resultSet1 = "INSERT INTO SharkAttackDatabase (userName, userPassword, userPassword2) VALUES (%s, %s, %s)"
        answer = (userName, userPassword, userPassword2)
        my_cursor.execute(resultSet1,answer)
        mydb.commit()
        #userMenu()
        #DB().insert_new_user_into_database()
        import usermenu

    elif (userPassword != userPassword2):
        print(" Passwords do not match, please try again")
        print("")
        createAccount()
        
        

    elif (userPassword is None):
        print(" Password Cannot Be Blank")
        print("")
        createAccount()
        
        #print("Please type your password!!")
        #userPassword = input("> ")
        #print("")
        #print("Please type your retype password!!")
        #userPassword2 = input("> ")
        #print(" Account has been created!!!")
        #print("")
        #userMenu()
    
    #Updating table with userName and password after creating a new account
    #val resultSet2 = statement.executeUpdate("INSERT INTO userAccount (userName, userPassword, userPassword2) VALUES ('"+userName+"', '"+userPassword+"',  '"+userPassword2+"');")
    #log.write("Executing 'INSERT INTO userAccount (userName, userPassword, userPassword2) VALUES ('"+userName+"', '"+userPassword+"',  '"+userPassword2+"');\n")


createAccount()