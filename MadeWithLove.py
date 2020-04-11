import csv

#Open csv file
with open(input("Enter file name: ")) as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    for row in readCSV: #Traverse the csv file
         #Open txt file, or create one if not exist
         with open('text.txt', 'a') as text_file:
             writeTXT = csv.writer(text_file, delimiter = ',')
             writeTXT.writerow(row) #Write each row to the new file
text_file.close()
