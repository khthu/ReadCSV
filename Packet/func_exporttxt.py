def export_txt():
    import csv
    with open('Output.csv', 'r') as read_csvfile: #Open csv input file
        readCSV = csv.reader(read_csvfile, delimiter = ',')
        for row in readCSV: #Traverve the csv file to write content to the txt file
            with open('Output.txt', 'a') as txtfile: #Open text file to write
                writeTXT = csv.writer(txtfile, delimiter = ',')
                writeTXT.writerow(row) #Write each row to the new file
