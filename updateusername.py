
from databaseupdates import databaseQueries
import sys
import os


#Change User Name in database
def changeUserName():
    global olduserName
    global newuserName
    
    
    print(" Type A OLD User Name")
    olduserName = input("> ")
    print("")
    if olduserName != "":
        print(" Type A NEW User Name")
        newuserName = input("> ")
        print("")
        databaseQueries().updateUserName()
    elif olduserName:
        print("Not a valid entry")
        changeUserName()
        
    elif newuserName == "":
        print(" Not a valid entry")
        changeUserName()
    
    
changeUserName()

