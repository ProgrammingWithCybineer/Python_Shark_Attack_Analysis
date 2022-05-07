import mysql.connector
import database
import pandas as pd

mycursor, commit = database.mysql_connection()


# Query for average age range of people attacked
def ageRangePeopleAttacked():
    print("")
    print("Average Age of Both Males & Female Attacked")
    print("")
    averageAgeAttacked = "SELECT sex, AVG(age) AS averageAgeAttacked FROM shark1 WHERE age IS NOT NULL AND sex IS NOT NULL GROUP BY sex"
    df = pd.read_sql(averageAgeAttacked, mycursor)
    #result.write.csv("results/avgAgePeopleAttacked")
    print(df)
    averageAgeAttacked.show()
    import usermenu


ageRangePeopleAttacked()
