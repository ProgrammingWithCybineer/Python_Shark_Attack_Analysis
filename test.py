import mysql.connector
import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql import HiveContext
import sqlalchemy as sa
import pandas as pd
import database
import mysql.connector
import sys
import os


import csv
with open('input\GSAF5.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)





