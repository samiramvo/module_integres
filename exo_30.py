import csv
f=open("file.csv","r")
reader=csv.reader(f)
next(reader)
for row in reader:
    print(row)