import mysql.connector
from mysql.connector import Error
import database
import pandas as pd
import numpy as np
import sys
import os
from database import DB



# This will run shark attack data and create the database with MySQL
DB().sharkAttackData()


#This will show first 100 rows from new table created in database 
DB().query_sharkdatabase()
