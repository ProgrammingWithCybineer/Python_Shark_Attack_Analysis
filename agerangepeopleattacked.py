import mysql.connector
from queries import typesOfQueries
import pandas as pd
import sys
import os
from usermenu import userQueryMenu



# Query for average age range of people attacked
def ageRangePeopleAttacked():
    
    typesOfQueries().avgAgePeopleAttacked()
    
    userQueryMenu()


ageRangePeopleAttacked()
