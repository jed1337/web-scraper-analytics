import csv
question1Output = []

with open('2014-2018.csv', 'r', errors='ignore') as csvFile:
     reader = csv.reader(csvFile)
     for row in sorted(reader, key=lambda row: (replaceNullInt(row[6]) * replaceNullFloat(row[7])), reverse=True):
         if "Mariah Carey" in row[3]:
            question1Output.append([row[0], row[1], row[3]])
            print("Year", row[0], "  Rank:" , row[1], "  Singer and Title:", row[3])

#print(question1Output)

csvFile.close()

