import database
import mysql.connector


mycursor, commit = database.mysql_connection()



#logging in as Admin
def adminLogIn():
    #val statement2 = connection.createStatement()
    print("Type Admin UserName")
    userAdmin = input("> ")
    print("")
    print("Type Admin Password")
    adminPassword = input("> ")
    print("")     
    resultSet2 = "SELECT COUNT(*) FROM adminAccount WHERE userAdmin=%s AND adminPassword= %s"
    #log.write("Executing 'SELECT COUNT(*) FROM adminAccount WHERE userAdmin='"+userAdmin+"' AND adminPassword='"+adminPassword+"');\n")
    answer6 = (userAdmin, adminPassword)
    mycursor.execute(resultSet2, answer6)
    commit
    
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