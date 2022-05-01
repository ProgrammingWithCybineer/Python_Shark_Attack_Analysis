
#Query for what shark is responsible for the most attacks
def sharkResponsible():
    print("What Shark is responsible for the most attacks...")
    result = hiveCtx.sql("SELECT (species) FROM shark1 WHERE species IS NOT NULL GROUP BY species ORDER BY COUNT(*) DESC")
    result.show()
    result.write.csv("results/sharkResponsible")
    #log.write("Executing 'SELECT (species) FROM shark1 GROUP BY species ORDER BY COUNT(*) DESC';\n")
    import usermenu

sharkResponsible()

