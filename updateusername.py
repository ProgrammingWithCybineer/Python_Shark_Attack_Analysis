from databaseupdates import databaseQueries



def changeUserName():
    global olduserName
    global newuserName
    
    
    print(" Type A OLD User Name")
    olduserName = input("> ")
    print("")
    print(" Type A NEW User Name")
    newuserName = input("> ")
    print("")
    
 
    databaseQueries().updateUserName()
    
    
changeUserName()

