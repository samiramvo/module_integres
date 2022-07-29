import csv
print("Ecrire des dictionnaires dans un fichier CSV:")
fw=open("test.csv","w",newline='')
writer=csv.DictWriter(fw,fieldnames=["Names","Class"])
writer.writeheader()
writer.writerow({"Names":"Samie","Class":"V"})
writer.writerow({"Names":"Saan","Class":"V"})
writer.writerow({"Names":"Saan","Class":"VI"})
fw.close()
fr=open("test.csv","r")
for row in fr:
    print(row)
fr.close()
