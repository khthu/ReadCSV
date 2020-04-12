import csv
import os

with open('text.txt') as check:
    if check is not None:
        os.remove('text.txt')
#Open csv file
with open('Book1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    for row in readCSV: #Traverse the csv file
         #Open txt file, or create one if not exist
         with open('text.txt', 'a') as text_file:
             writeTXT = csv.writer(text_file, delimiter = ',')
             if row[5]=='Recommend':
                 row.append('SCKT')
                 row.append('KTSC')
             else:
                 row.append('16')
                 row.append('26')
             writeTXT.writerow(row) #Write each row to the new file

with open('text.txt', 'a') as text_file:
    writeTXT = csv.writer(text_file, delimiter = ',')
    new_row = list()
    for i in range(len(row)):
        row[i]= '168'
        new_row.append(row[i])
    writeTXT.writerow(new_row)

print('Done!')
text_file.close()
