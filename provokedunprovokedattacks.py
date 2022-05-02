import sharkAnalysis
import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark import HiveContext



#Query for the number of provoked and unprovoked shark attacks
def provokedUnprovokedAttacks():
    print("Number of Provoked and Unprovoked Attacks")
    result = hiveCtx.sql("SELECT type, Count(type) AS whichTypeMost FROM shark1 WHERE type IS NOT NULL GROUP BY type ORDER BY whichTypeMost DESC")
    result.show()
    result.write.csv("results/provokedUnprovokedAttacks")
    #log.write("Executing 'SELECT typeAttack, Count(typeAttack) AS whichTypeMost FROM shark1 GROUP BY typeAttack ORDER BY whichTypeMost';\n")
    import usermenu
