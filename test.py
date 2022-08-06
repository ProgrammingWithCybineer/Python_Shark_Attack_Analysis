from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql import HiveContext
import sqlalchemy as sa
import pandas as pd


#This is just a test file use I use to test reading from a CSV file
import csv
with open('input\GSAF51.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)





