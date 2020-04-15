def add_column_csv():
    import csv
    with open('Input.csv', 'r') as read_csvfile:
        with open('Output.csv', 'a') as write_csvfile:
            readCSV = csv.reader(read_csvfile, delimiter = ',') #Open reader
            writeCSV = csv.writer(write_csvfile, delimiter = ',') #Open writer
            #Add column's header
            all = []
            row = next(readCSV)
            row.append('SCKT')
            row.append('KTSC')
            writeCSV.writerow(row)
            #all.append(row)
            #Add column's other values
            for row in readCSV: #Traverse the csv file to add new columns
                row.append('16')
                row.append('26')
                #all.append(row)
                #Write all changes to row
                writeCSV.writerow(row) #Write changes

#add_column_csv()
