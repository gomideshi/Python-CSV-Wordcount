#Read the file line by line
#Append the values for location to a list
#Build a set of uniques from that list
#Determine the count for each of the uniques in the list

import csv
from collections import Counter

with open('readsample.csv', 'rb') as f:
    reader = csv.reader(f)
    reader.next()
    names = [row[2] for row in reader]

    for (k,v) in Counter(names).iteritems():
        print "%s appears %d times" % (k, v)
