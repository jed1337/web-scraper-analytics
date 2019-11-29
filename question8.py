import pandas as pd
#Read csv
df = pd.read_csv("2014-2018.csv")

# Groupby and sum
df_new = df.groupby(["Year", "Artist and Title"]).agg({"TPts": "sum"}).sort_values(["Year", "Artist and Title"]).sort_values(by=['TPts'], ascending=False ).iloc[0:7]
print(df_new)
