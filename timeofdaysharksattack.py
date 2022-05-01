    
#STILL NEED TO FIGURE OUT THIS QUERY
# Query for what time of day do most shark attacks occur
def timeOfDaySharkAttack():
    print("Time most shark attacks occur...")
    #val result = hiveCtx.sql("SELECT COUNT(year) FROM shark1 WHERE year > 999") // STILL NEED TO FIGURE OUT THIS QUERY
    #val result1 = hiveCtx.sql("CREATE VIEW AvgTimeOfAttacked AS SELECT time, CONVERT(SUBSTRING(time,1,2), UNSIGNED INTEGER) AS timeConvert FROM shark1")
    result1 = hiveCtx.sql("CREATE VIEW IF NOT EXISTS AvgTimeOfAttacked AS SELECT CAST(regexp_replace(time, 'h00', '') AS int) AS time FROM shark1 WHERE time IS NOT NULL LIMIT 10")
    result2 = hiveCtx.sql("SELECT AVG(time) FROM AvgTimeOfAttacked WHERE time IS NOT NULL")
    #result.show()
    #result.write.csv("results/timeOfDaySharkAttack")
    result2.show()
    result2.write.csv("results/timeOfDaySharkAttack")
    #log.write("Executing 'NEED TO ADD LOG HERE');\n")
    
#cast(str_column as int)
    import usermenu


timeOfDaySharkAttack()