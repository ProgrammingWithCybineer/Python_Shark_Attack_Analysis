


    
# Query for total number of shark attacks since certain date
def totalSharkAttacks():
    print("Total number of attacks recorded...")
    result = hiveCtx.sql("SELECT COUNT(year) AS TotalAttacks FROM shark1 WHERE year > 1950")
    result.show()
    result.write.csv("results/totalSharkAttacks")
    #log.write("Executing 'SELECT COUNT(year) FROM shark1 WHERE year > 1950';\n")
    import usermenu

totalSharkAttacks()

