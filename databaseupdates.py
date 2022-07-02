from database import DB
import pandas as pd
import sys
import os


class databaseQueries(DB):
    
    def updateUserName(self):
        from updateusername import olduserName, newuserName
        if self.mydb.is_connected():
            resultSet2_1 = ("UPDATE SharkAttackDatabase SET userName = %s WHERE userName = %s")
            answer2_1 = (newuserName, olduserName)
            mycursor = self.mydb.cursor()
            mycursor.execute(resultSet2_1, answer2_1)
            self.mydb.commit()
            print("User Name Updated")
            import userchoice
  
   
            
    def updateUserPassword(self):
        from updateuserpassword import userName, newUserPassword
        if self.mydb.is_connected():
            resultSet2_1 = ("UPDATE SharkAttackDatabase SET userPassword = %s, userPassword2 = %s WHERE userName = %s")
            answer2_1 = (newUserPassword, newUserPassword, userName)
            mycursor = self.mydb.cursor()
            mycursor.execute(resultSet2_1, answer2_1)
            self.mydb.commit()
            print("User Password Updated")
            import userchoice
  
            
    
    def listUsers(self):
       if self.mydb.is_connected():
            listUsers = "SELECT user_id, userName FROM SharkAttackDatabase"
            mycursor = self.mydb.cursor()
            mycursor.execute(listUsers)
            resultSet4 = mycursor.fetchall()
            for x in resultSet4:
                print(x)
 
  
              
    def updateDeleteUser(self):
        from deleteuser import userName
        if self.mydb.is_connected():
            resultSet5 =  "DELETE FROM SharkAttackDatabase WHERE userName = %s "
            answer6 = (userName,)
            mycursor = self.mydb.cursor()
            mycursor.execute(resultSet5, answer6)
            self.mydb.commit()
            print("User {} has been deleted.".format(userName))
            import adminmenu 