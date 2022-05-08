import mysql.connector
import database

#mycursor, commit = database.mysql_connection()



#Create User Account    
def createAccount():    
    
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
        #resultSet12 = "INSERT INTO SharkAttackDatabase (userName, userPassword, userPassword2) VALUES (%s, %s, %s)"
        #answer = (userName, userPassword, userPassword2)
        #mycursor.execute(resultSet12,answer)
        #commit
        
        
        #answer = (userName, userPassword, userPassword2)
        #mycursor.execute(resultSet1,answer)
        #mydb.commit() 
        
        import usermenu

    elif (userPassword != userPassword2):
        print(" Passwords do not match, please try again")
        print("")
        createAccount()
        
        

    elif (userPassword is None):
        print(" Password Cannot Be Blank")
        print("")
        createAccount()
        
        
              
createAccount()