from databaseupdates import databaseQueries
import sys
import os




def changeUserPassword():
    global userName
    global oldUserPassword
    global newUserPassword
    
    print("Type User Name")
    userName = input("> ")
    print("")
    print(" Type A OLD Password")
    oldUserPassword = input("> ")
    print("")
    print(" Type A NEW Password")
    newUserPassword = input("> ")
    print("")
    
 
    databaseQueries().updateUserPassword()
    
    
changeUserPassword()
