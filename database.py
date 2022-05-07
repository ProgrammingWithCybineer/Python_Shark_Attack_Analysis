import mysql.connector


# Create Cursor Instance
#my_cursor = mydb.cursor()
#global userName
#global userPassword
#global userPassword2   

#class DB:
    # def __del__(self):
        #self.mydb.close()
        

    # def __init__(self):
        #self.mydb = mysql.connector.connect(
            #host = "localhost",
            #user = "root",
            #passwd = "####################",#### REMOVE BEFORE COMMITING CODE
            #database = "Shark_Attack_Login",
        #)
        #print("Started database connection")
        


    #this will insert into database newly created user
    # def insert_new_user_into_database(self):
        #mycursor = self.mydb.cursor()
        ## NEED TO CREATE SHARKATTACHDATABASE  DATABASE IN MYSQL ######
        #resultSet1 = "INSERT INTO SharkAttackDatabase (userName, userPassword, userPassword2) VALUES (%s, %s, %s)"
        #answer = (userName, userPassword, userPassword2)
        #mycursor.execute(resultSet1,answer)
        #mycursor.commit()
        #userMenu()
        
        #mycursor.close()



    # def do_that_with_connection(self):
    # def connect_to_mysql(self):
        #mycursor = self.mydb.cursor()
        #mydb = mysql.connector.connect(
        #host = "localhost",
        #user = "root",
        #passwd = "#################",#### REMOVE BEFORE COMMITING CODE
        #database = "Shark_Attack_Login",
        #)
        #print(mydb)


        # Create Cursor Instance
        #mycursor = mydb.cursor()
        #mycursor.close()
        
        
        
        
        

def mysql_connection():
    mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "##########################",#### REMOVE BEFORE COMMITING CODE
    database = "Shark_Attack_Login",
    )
    #print(mydb)


    # Create Cursor Instance
    mycursor = mydb.cursor()
    commit = mydb.commit()
    mycursor.close()
    return mycursor, commit
    
        
        
 




