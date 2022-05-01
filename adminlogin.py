


#logging in as Admin
def adminLogIn():
    #val statement2 = connection.createStatement()
    print("Type Admin UserName")
    userAdmin = input("> ")
    print("")
    print("Type Admin Password")
    adminPassword = input("> ")
    print("")     
    resultSet2 = statement.executeQuery("SELECT COUNT(*) FROM adminAccount WHERE userAdmin='"+userAdmin+"' AND adminPassword='"+adminPassword+"';")
    #log.write("Executing 'SELECT COUNT(*) FROM adminAccount WHERE userAdmin='"+userAdmin+"' AND adminPassword='"+adminPassword+"');\n")
    while ( resultSet2.next() ): 
        if (resultSet2.getString(1) == "1"):
            print(" Log In Successful!!")
            #adminMenu()
            import adminmenu
        else:
            print("Username/password combo not found. Try again!")
            print("")
            adminLogIn()
            
            
adminLogIn()