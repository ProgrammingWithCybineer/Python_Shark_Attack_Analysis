#import database
import mysql.connector
import ast
from database import DB
import sys
import os



#User logging in
def userLogIn():
     
    global userName
    global userPassword    
    
    print(" Please type a UserName")
    userName = input("> ")
    print("")
    print(" Please type A Password")
    userPassword = input("> ")
    
    #DB().verifyUserLogin()
    DB().loginVerifyUser()
    
userLogIn()