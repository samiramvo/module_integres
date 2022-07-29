import csv
f=open("test.csv","w",newline='')
f.write("abcd")
f.write("bcde")

fr=open("test.csv","r")
for row in fr:
    print(row)
fr.close()
