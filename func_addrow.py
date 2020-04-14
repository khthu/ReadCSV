def add_row_csv():
    import csv
    with open('Input.csv', 'r') as read_csvfile:
        with open('Output.csv', 'a') as write_csvfile:
            readCSV = csv.reader(read_csvfile, delimiter = ',')
            writeCSV = csv.writer(write_csvfile, delimiter = ',')
            for row in readCSV:
                writeCSV.writerow(row)
            new_row = list()
            for i in range(len(row)):
                row[i]= '168'
                new_row.append(row[i])
            writeCSV.writerow(new_row)

add_row_csv()
