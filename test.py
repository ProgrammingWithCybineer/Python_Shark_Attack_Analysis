

import csv
with open('input\GSAF5 (1_2).csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)