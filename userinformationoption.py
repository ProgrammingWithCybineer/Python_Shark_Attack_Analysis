from multiprocessing.connection import answer_challenge
import database
import mysql.connector


mycursor, commit = database.mysql_connection()

#Update/ change User name and/or userpassword
def userInformationOption():
    global userName
    global userNameUpdate
    global userPasswordUpdate
    global userPasswordUpdate2
    print("")
    print("################################")
    print(" (1) Update User Name ")
    print("")
    print(" (2) Update User Password")
    print("")
    print(" (3) Previous Menu ")
    print("")
    print(" (0) Exit the program ")
    print("")
    print("#################################")
    choice2 =  input(int("> "))
    
    if (choice2 == 1):
        print(" Type A New User Name")
        userNameUpdate = input("> ")
        resultSet2_1 = ("UPDATE userAccount SET userName = %s WHERE userName = %s")
        answer2_1 = (userNameUpdate, userName)
        mycursor.execute(resultSet2_1, answer2_1)
        commit
        #log.write("UPDATE userAccount SET userName = ('"+userNameUpdate+"') WHERE username = ('"+userName+"') \n")
        print("User Name Updated")
        #userChoice()
        import userchoice
        

## STILL WORKING ON THIS SECTION ####
    elif (choice2 == 2):
        print("Type User Name")
        userName = input("> ")
        print(" Type A New Password")
        userPasswordUpdate = input("> ")
        #resultSet2_2 = statement.executeUpdate("UPDATE userAccount SET userPassword = ('"+userPasswordUpdate+"') WHERE userName = ('"+userName+"');")
        #log.write("UPDATE userAccount SET userPassword = ('"+userPasswordUpdate+"') WHERE username = ('"+userName+"') \n")
        print(" ReType Password")
        userPasswordUpdate2 = input("> ")
        #resultSet2_3 = statement.executeUpdate("UPDATE userAccount SET userPassword2 = ('"+userPasswordUpdate2+"') WHERE userName = ('"+userName+"');")
        #log.write("UPDATE userAccount SET userPassword2 = ('"+userPasswordUpdate2+"') WHERE username = ('"+userName+"') \n")
        print("User Name Updated")
        #userChoice()
        import userchoice

    elif (choice2 == 3):
        #userChoice()
        import userchoice

    elif (choice2 == 0):
        #exitProgram()
        import exitprogram
    
    elif (( choice2 != 0 or choice2 != 1 or choice2 != 2 or choice2 != 3)): 
        print(" Not a valid choice, please try again!!!")
        #userChoice()
        import userchoice
        
        
        
        
        
userInformationOption()
 