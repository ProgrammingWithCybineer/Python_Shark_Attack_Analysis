


# Query for location of most shark attacks
def locationMostSharksAttacks():
    print("Location of Most Shark Attack...")
    result = hiveCtx.sql("SELECT (country) FROM shark1 WHERE country IS NOT NULL GROUP BY country ORDER BY COUNT(*) DESC")
    result.show()
    result.write.csv("results/locationMostSharksAttacks")
    #log.write("Executing 'SELECT (country) FROM shark1 WHERE country IS NOT NULL GROUP BY country ORDER BY COUNT(*) DESC';\n")
    import usermenu



locationMostSharksAttacks()