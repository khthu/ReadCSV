import csv

with open(input("Enter file name: ")) as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    for row in readCSV:
         print(row)