# import csv
# question1Output = []

# with open('consolidated.csv', 'r', errors='ignore') as csvFile:
#      reader = csv.reader(csvFile)
#      for row in sorted(reader, key=lambda row: (replaceNullInt(row[6]) * replaceNullFloat(row[7])), reverse=True):
#          if "Mariah Carey" in row[3]:
#             question1Output.append([row[0], row[1], row[3]])
#             print("Year", row[0], "  Rank:" , row[1], "  Singer and Title:", row[3])
 
# csvFile.close()


import pandas as pd
#Read csv
def question5():
   df = pd.read_csv("consolidated.csv")
   # Groupby and sum
   df_new = df.groupby(["Year", "Artist and Title"]).agg({"Pts+": "sum"}).sort_values(["Year", "Artist and Title"]).sort_values(by=['Pts+'], ascending=True ).iloc[0:10]
   print(df_new)


