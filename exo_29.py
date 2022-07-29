import csv
f=open("file.csv",newline='')
csv_reader=csv.reader(f)
print(next(csv_reader))