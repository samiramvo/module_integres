import csv
csv_string="""2,8,7,6,0,5,4"""
lines=csv_string.splitlines()
print(lines)

reader=csv.reader(lines)
print(list(reader))