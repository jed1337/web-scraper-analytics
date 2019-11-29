import pandas as pd
#Read csv
def question7():
    df = pd.read_csv("consolidated.csv")

    # Groupby and sum
    df_new = df.groupby(["Year", "Artist and Title"]).agg({"TPts": "sum"}).sort_values(["Year", "Artist and Title"]).sort_values(by=['TPts'], ascending=True ).iloc[0:10]
    print(df_new)
