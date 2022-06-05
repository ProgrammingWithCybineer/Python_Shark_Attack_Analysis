from database import DB
import pandas as pd


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