

# Query for average age range of people attacked
def ageRangePeopleAttacked():
    print("Average Age of Both Males & Female Attacked")
    result = hiveCtx.sql("SELECT sex, AVG(age) AS averageAgeAttacked FROM shark1 WHERE age IS NOT NULL AND sex IS NOT NULL GROUP BY sex")
    result.show()
    result.write.csv("results/avgAgePeopleAttacked")
    #result.write.mode(SaveMode.Overwrite).csv("results/avgAgePeopleAttacked")
    #log.write("Executing 'SELECT sex, AVG(age) AS averageAgeAttacked FROM shark1 GROUP BY sex';\n")
    import usermenu


ageRangePeopleAttacked()
