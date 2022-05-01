


#User logging in
def userLogIn():
    print(" Please type a User Name")
    userName = input("> ")
    print("")
    print(" Please type A Password")
    userPassword = input("> ")
    resultSet = statement.executeQuery("SELECT COUNT(*) FROM userAccount WHERE userName='"+userName+"' AND userPassword='"+userPassword+"';")
    #log.write("Executing 'SELECT COUNT(*) FROM userAccount WHERE userName='"+userName+"' AND userPassword='"+userPassword+"');\n")
    while ( resultSet.next()):
        if (resultSet.getString(1) == "1"):
            print("You Have Logged In Successfully")
            #userChoice()
            import userchoice
            
        else:
            print("Username/password combo not found. Try again!")
            userLogIn()



userLogIn()