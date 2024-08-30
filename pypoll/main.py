import os
import csv
poll_csv = os.path.join('..'),'Resources','election_data.csv')
with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    
