def add_row_csv(leng):
    import csv
    with open('Input.csv', 'r') as read_csvfile:
        with open('Output.csv', 'a') as write_csvfile:
            readCSV = csv.reader(read_csvfile, delimiter = ',')
            writeCSV = csv.writer(write_csvfile, delimiter = ',')
            #for row in readCSV:
            #    writeCSV.writerow(row)
            i = 0
            new_row = list()
            for i in range(leng):
                new_row.append('168')
            writeCSV.writerow(new_row)

#add_row_csv()
