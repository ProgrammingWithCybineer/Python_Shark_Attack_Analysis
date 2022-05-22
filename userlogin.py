import database
import mysql.connector
import ast
from database import DB



 

#User logging in
def userLogIn():
    DB().userLoginDatabaseConnection()
    global userName
    global userPassword    
    
    print(" Please type a User Name")
    userName = input("> ")
    print("")
    print(" Please type A Password")
    userPassword = input("> ")
    DB().verifyUserLogin()
    
userLogIn()