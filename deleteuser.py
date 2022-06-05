from databaseupdates import databaseQueries



#DELETE USER 
def deleteUser():
    global userName
    #global userID
    print("")
    print("################################")
    print(" (1) Choose A User To Delete ")
    print("")
    print(" (2) Exit the program")
    print("")
    print("#################################")
    choice2 = int(input("> "))
     
    if (choice2 == 1):
        databaseQueries().listUsers()
        print("")
        print(" Type A User's Name")
        userName =  input("> ")
        print("")
        
        databaseQueries().updateDeleteUser() 

    elif (choice2 == 2):
        print(" choice 2.")
        import exitprogram
    
    elif (( choice2 != 1 or choice2 != 2 )):
        print(" Not a valid choice, please try again!!!")
        deleteUser()
    


deleteUser()