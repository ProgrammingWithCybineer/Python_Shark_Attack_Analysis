from database import DB
import mysql.connector
import sys
import os
import pandas as pd



class typesOfQueries(DB):
    
    def totalnumbersharkattacks(self):
        if self.mydb.is_connected():
            totalSharkAttacks = "SELECT COUNT(year) AS TotalAttacks FROM SharkAttackTable WHERE year > 1950"
            mycursor = self.mydb.cursor()        
            mycursor.execute(totalSharkAttacks)
            output = mycursor.fetchall()
            for x in output:
                print(x)
                print("Back to User Query menu")
        
    
    
    def avgAgePeopleAttacked(self):
        if self.mydb.is_connected():
            averageAgeAttacked = "SELECT sex, AVG(age) AS averageAgeAttacked FROM SharkAttackTable WHERE age IS NOT NULL AND sex IS NOT NULL GROUP BY sex"
            mycursor = self.mydb.cursor()
            mycursor.execute(averageAgeAttacked)
            output = mycursor.fetchall()
            for x in output:
                print(x)
                import usermenu
    
        
    
    def locationSharkAttacksHappen(self):
        if self.mydb.is_connected():
            locationMostSharksAttacks = "SELECT (country) FROM sharkattacktable WHERE country IS NOT NULL GROUP BY country ORDER BY COUNT(*) DESC;"
            mycursor = self.mydb.cursor()
            mycursor.execute(locationMostSharksAttacks)
            output = mycursor.fetchall()
            for x in output:
                print(x)
                import usermenu
    
 
   
    def sharkResponsibleMostAttack(self):
        if self.mydb.is_connected():
            sharkMostResponsible = "SELECT (species) FROM SharkAttackTable WHERE species IS NOT NULL GROUP BY species ORDER BY COUNT(*) DESC"                 
            mycursor = self.mydb.cursor()
            mycursor.execute(sharkMostResponsible)
            output = mycursor.fetchall()
            for x in output:
                print(x)
                import usermenu
                
            
    def timeMostSharkAttacksHappen(self):
        if self.mydb.is_connected():
            timeOfDaySharkAttack1 = "CREATE VIEW IF NOT EXISTS SharkAttackTable AS SELECT CAST(regexp_replace(time, 'h00', '') AS int) AS time FROM SharkAttackTable WHERE time IS NOT NULL"
            timeOfDaySharkAttack1 = "SELECT AVG(time) FROM SharkAttackTable WHERE time IS NOT NULL"
            #timeOfDaySharkAttack1 = "SELECT SEC_TO_TIME(AVG(TIME_TO_SEC(`time`))) FROM SharkAttackTable"        
            mycursor = self.mydb.cursor()        
            mycursor.execute(timeOfDaySharkAttack1)
            output = mycursor.fetchall()
            for x in output:
                print(x)
                import usermenu
    
    
          
    def unprovokedVsProvokedAttacks(self):
        if self.mydb.is_connected():
            provokedUnprovoked = "SELECT typeAttack, Count(typeAttack) AS whichTypeMost FROM SharkAttackTable WHERE typeAttack IS NOT NULL GROUP BY typeAttack ORDER BY whichtypeMost DESC"
            mycursor = self.mydb.cursor()
            mycursor.execute(provokedUnprovoked)
            output = mycursor.fetchall()
            for x in output:
                print(x)
                import usermenu
    
    
 
    