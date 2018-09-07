import matplotlib.pyplot as plt
import csv

"""Plot the number of matches played in each season through the years in IPL

This module demonstrates reading a csv file and adding up values from individual entries and printing its total value.

Attributes:
    matches_dataset (string): string storing the path to the csv file which contains the data for all the IPL matches

    fields (list): list of headers

    rows (list): list of lists contains rows from the csv file. Each row in turn is a list of various column items

    count (int): counter for number of matches played in a season

    season (int): stores the current season counting operation is going on in
"""

fields = []
rows = []
matches_dataset = 'matches.csv'

"""open csv file and read it"""
with open(matches_dataset, 'r') as matches_csvfile:
    reader = csv.reader(matches_csvfile, delimiter=',')

    """next() reads one row and moves pointer to next row. fields stores headers"""
    fields = next(reader)

    """store all rows into list rows"""
    for row in reader:
        rows.append(row)

# print("total no. of rows: %d" %(reader.line_num))
# print(fields)

count = 0
season = 0

"""loop to count matches each season and print a bar for it"""
for row in rows:
    if int(row[1]) != season:
        if season != 0:
            plt.bar(season, count)
        season = int(row[1])
        count = 0
    count += 1
plt.bar(season, count)

"""display the matplotlib output"""
plt.show()
