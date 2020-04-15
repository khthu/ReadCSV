import csv
from func_addcolumn import add_column_csv
from func_addrow import add_row_csv
from func_exporttxt import export_txt

add_column_csv()

with open('Output.csv','r') as readCSV:
    readCSV = csv.reader(readCSV, delimiter = ',')
    for row in readCSV:
        leng = len(row)

add_row_csv(leng)
export_txt()
