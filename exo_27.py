import csv
reader=csv.reader(open("file.csv"))
lines=len(list(reader))
print(lines)