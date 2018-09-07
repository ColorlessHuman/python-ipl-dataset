# import matplotlib.pyplot as plt
import numpy
import csv

matches_dataset = 'matches.csv'
matches_data = open(matches_dataset, 'rt')
reader = csv.reader(matches_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('float')
print(data.shape)
