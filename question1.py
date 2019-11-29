import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import csv

def question1():
    data = pd.read_csv("consolidated.csv")
    top_artists = data[['Artist and Title', 'Year', 'TPts']].sort_values(by=['Year','TPts'],ascending=False).groupby(['Year']).head(5)
    print(top_artists.groupby('Artist and Title')['Year'].count())
