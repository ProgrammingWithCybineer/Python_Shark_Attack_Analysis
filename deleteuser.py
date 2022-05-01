
#DELETE USER 
def deleteUser():
    global userName
    print("")
    print("################################")
    print(" (1) Choose A User To Delete ")
    print("")
    print(" (2) Exit the program")
    print("")
    print("#################################")
    choice2 = int(input("> "))
     
    if (choice2 == 1):
        resultSet4 = statement.executeQuery("SELECT * FROM userAccount")
        #log.write("Executing 'SELECT * FROM userAccount';\n")
        print(" Type A User's Name")
        userName =  input("> ")
        resultSet3 =  statement.executeUpdate("DELETE FROM userAccount WHERE userName = ('"+userName+"');")
        #log.write("Executing 'DELETE User from database' \n")
        print("User Deleted")
        resultSet5 = statement.executeQuery("SELECT * FROM userAccount")
        #log.write("Executing 'SELECT * FROM userAccount';\n")
        #adminMenu()
        import adminmenu 

    elif (choice2 == 2):
        print(" choice 2.")
        #exitProgram()
        import exitprogram
    
    elif (( choice2 != 1 or choice2 != 2 )):
        print(" Not a valid choice, please try again!!!")
        deleteUser()
    


deleteUser()