import mysql.connector
import sqlalchemy
import database
import pandas as pd
import csv


mycursor, commit = database.mysql_connection()



#Query for location of most shark attacks
def locationMostSharksAttacks():
    print("Location of Most Shark Attack...")
    locationMostSharksAttacks = pd.read_csv("input\GSAF5.csv")
    locationMostSharksAttacks = pd.DataFrame("CREATE TABLE IF NOT EXISTS shark1 (caseNumber STRING, date STRING, year INT, type STRING, country STRING, area STRING, location STRING, activity STRING, name STRING, sex STRING, age INT, injury STRING, fatal STRING, time STRING, species STRING, investigator_or_source STRING, pdf STRING, href_formula STRING, href_ STRING, case_number1 STRING, case_number STRING, original_order INT)")
    locationMostSharksAttacks.query = "SELECT (country) FROM GSAF5 WHERE country IS NOT NULL GROUP BY country ORDER BY COUNT(*) DESC"
    # df1 = pd.read_sql(locationMostSharksAttacks, mycursor)
    print(locationMostSharksAttacks)
    #locationMostSharksAttacks.head()
    

    
    #result.write.csv("results/locationMostSharksAttacks")
    #log.write("Executing 'SELECT (country) FROM shark1 WHERE country IS NOT NULL GROUP BY country ORDER BY COUNT(*) DESC';\n")
    #import usermenu
 
    import usermenu

locationMostSharksAttacks()