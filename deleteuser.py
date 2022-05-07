import database
import mysql.connector

mycursor, commit = database.mysql_connection()


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
        mycursor.execute("SELECT * FROM userAccount")
        resultSet4 = mycursor.fetchall()
        for x in resultSet4:
            print(x)
        
        #log.write("Executing 'SELECT * FROM userAccount';\n")
        print(" Type A User's Name")
        userName =  input("> ")
        #resultSet3 =  statement.executeUpdate("DELETE FROM userAccount WHERE userName = ('"+userName+"');")
        resultSet5 =  "DELETE FROM userAccount WHERE userName = %s"
        #log.write("Executing 'DELETE User from database' \n")
        answer6 = (userName)
        mycursor.execute(resultSet5, answer6)
        commit
        print("User Deleted")
        mycursor.execute("SELECT * FROM userAccount")
        resultSet6 = mycursor.fetchall()
        for x in resultSet6:
            print(x)
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