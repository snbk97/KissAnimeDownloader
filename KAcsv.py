import csv

fo = open('anime_links.csv', 'rb')

reader = csv.reader(fo, delimiter='~')

for row in reader:
    print row[1]+"\n"

'''
A little Demo snippet to extract links from csv

'''
