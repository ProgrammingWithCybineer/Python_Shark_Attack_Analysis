from database import DB
import mysql.connector
import sys
import os
import pandas as pd


#Classes for queries regarding shark data
class typesOfQueries(DB):
    
    def totalnumbersharkattacks(self):
        if self.mydb.is_connected():
            totalSharkAttacks = "SELECT COUNT(year) AS TotalAttacks FROM SharkAttackTable WHERE year > 1921"
            mycursor = self.mydb.cursor()        
            mycursor.execute(totalSharkAttacks)
            output = mycursor.fetchall()
            df = pd.DataFrame(columns=["Total Attacks"],data=output)
            print(df)
    
      
    
    def locationSharkAttacksHappen(self):
        if self.mydb.is_connected():
            locationMostSharksAttacks = "SELECT (country), Count(country) FROM sharkattacktable WHERE country IS NOT NULL GROUP BY country ORDER BY COUNT(*) DESC;"
            mycursor = self.mydb.cursor()
            mycursor.execute(locationMostSharksAttacks)
            output = mycursor.fetchmany(50)
            df = pd.DataFrame(columns=["Country","Total Number Of Attacks"],data=output)
            print(df)
                
    
   
    def sharkResponsibleMostAttack(self):
        if self.mydb.is_connected():
            sharkMostResponsible = '''SELECT (species), Count(species) FROM SharkAttackTable WHERE species NOT LIKE "%INVALID" AND species NOT LIKE "%Shark involvement prior to death was not confirmed" AND 
                                    species NOT LIKE "%Shark involvement not confirmed" AND species NOT LIKE "%Questionable incident" AND species NOT LIKE "%No shark involvement"
                                    AND species NOT LIKE "%Shark involvement prior to death unconfirmed" AND species NOT LIKE "%Shark involvement prior to death not confirmed" AND species IS NOT NULL GROUP BY species ORDER BY COUNT(*) DESC;'''                 
            mycursor = self.mydb.cursor()
            mycursor.execute(sharkMostResponsible)
            output = mycursor.fetchmany(50)
            df = pd.DataFrame(columns=["Species","Total Number Of Sharks"],data=output)
            print(df) 
            
              
                
    # Need to Convert time to show accurately******        
    def timeMostSharkAttacksHappen(self):
        if self.mydb.is_connected():
            #timeOfDaySharkAttack1 = "CREATE VIEW IF NOT EXISTS SharkAttackTable AS SELECT CAST(regexp_replace(time, 'h00', '') AS int) AS time FROM SharkAttackTable WHERE time IS NOT NULL"
            #timeOfDaySharkAttack1 = "SELECT AVG(time) FROM SharkAttackTable WHERE time IS NOT NULL"
            timeOfDaySharkAttack1 = "SELECT SEC_TO_TIME(AVG(TIME_TO_SEC(`time`))) FROM SharkAttackTable;"  
                                        
            mycursor = self.mydb.cursor()        
            mycursor.execute(timeOfDaySharkAttack1)
            output = mycursor.fetchall()
            for x in output:
                print(x)
     
    
          
    def unprovokedVsProvokedAttacks(self):
        if self.mydb.is_connected():
            provokedUnprovoked = "SELECT typeAttack, Count(typeAttack) FROM SharkAttackTable WHERE typeAttack IS NOT NULL GROUP BY typeAttack ORDER BY COUNT(*) DESC;"
            mycursor = self.mydb.cursor()
            mycursor.execute(provokedUnprovoked)
            output = mycursor.fetchall()
            df = pd.DataFrame(columns=["Provoked/Unprovoked","Total Number of Attacks"],data=output)
            print(df)
     
 
      
    def avgAgePeopleAttacked(self):
        if self.mydb.is_connected():
            averageAgeAttacked = "SELECT sex, AVG(age) AS averageAgeAttacked FROM SharkAttackTable WHERE age IS NOT NULL AND sex IS NOT NULL GROUP BY sex"
            mycursor = self.mydb.cursor()
            mycursor.execute(averageAgeAttacked)
            output = mycursor.fetchall()
            df = pd.DataFrame(columns=["Sex","Age"],data=output)
            print(df)
                
                
    