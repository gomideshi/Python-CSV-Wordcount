#--------------------------------------------------------------------
# TODO:
#   - lowercase() the contents of an early data set to prevent dupes
#   - filter (re.sub?) non alpha-numeric from early data set
#--------------------------------------------------------------------

import csv, itertools

#Prompt for file / count
file_name = raw_input('File name? (omit .csv) ')
list_count = input('How many positions are needed? (5, 10, 25, etc.) ')
                   
#Read the contents of 'readsample.csv' and begin splitting it
incoming_data = open(file_name + '.csv', 'r').read().split()
delimited_data = [item.split(',') for item in incoming_data]

#Recombine the contents of the list into one meta list
remerged = list(itertools.chain(*delimited_data))

#Count the frequency of each word, and pair it as a dict entry
wordfreq = [remerged.count(p) for p in remerged]
dictionary = dict(zip(remerged, wordfreq))

#For each pair, sort by key (wordfreq) and reverse to top-down
aux = [(dictionary[key], key) for key in dictionary]
aux.sort()
aux.reverse()

#For the top 25 entries, print them
for a in aux[:list_count]:
    print a
