# main PyPoll file
import csv
from numpy import mean
import statistics
with open('Resources/election_data1.csv') as file:
    reader = csv.DictReader(file, delimiter=',')
