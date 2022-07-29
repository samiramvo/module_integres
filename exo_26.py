import csv
reader=csv.reader(open("arduino-cli.csv"))
for col in reader:
    print(col)