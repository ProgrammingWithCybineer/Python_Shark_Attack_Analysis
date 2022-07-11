from database import DB
import sys
import os



def createUserAccount():
    
    global userName
    global userPassword 
    global userPassword2
      
         
    print("")
    print("Please type your username")
    userName = input("> ")
    print("")
    print("Please type your password")
    userPassword = input("> ")
    print("")
    print("Please type your retype password")
    userPassword2 = input("> ")
        
       
    
    #DB().connectToDatabase()  
    DB().addUserToDatabase()

        
              
createUserAccount()
