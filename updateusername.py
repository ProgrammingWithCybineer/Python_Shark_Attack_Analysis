
from databaseupdates import databaseQueries
import sys
import os



def changeUserName():
    global olduserName
    global newuserName
    
    
    print(" Type A OLD User Name")
    olduserName = input("> ")
    print("")
    if olduserName.isalpha():
        print(" Type A NEW User Name")
        newuserName = input("> ")
        print("")
    elif olduserName.isdigit():
        print("Not a valid entry")
        changeUserName()
        if newuserName.isalpha():
            databaseQueries().updateUserName()
        elif newuserName.isdigit():
            print(" Not a valid entry")
            changeUserName()
            
            
            
   
    
changeUserName()

