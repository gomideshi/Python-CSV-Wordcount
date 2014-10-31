data = \
"""
Demo,Demo,Jim
Demo,Demo,John
Demo,Demo,John
Demo,Demo,Jake
Demo,Demo,Jake
Demo,Demo,John
"""

import csv
import StringIO
from collections import Counter


input_stream = StringIO.StringIO(data)
reader = csv.reader(input_stream, delimiter=',')

reader.next()
cities = [row[2] for row in reader]

for (k,v) in Counter(cities).iteritems():
    print "%s appears %d times" % (k, v)
