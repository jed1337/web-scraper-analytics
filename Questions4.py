import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df_2018 = pd.read_csv("C:/Users/artiele/Downloads/20181225.csv")
df_2017 = pd.read_csv("C:/Users/artiele/Downloads/20171225.csv")
df_2016 = pd.read_csv("C:/Users/artiele/Downloads/20161225.csv")
df_2015 = pd.read_csv("C:/Users/artiele/Downloads/20151225.csv")
df_2014 = pd.read_csv("C:/Users/artiele/Downloads/20141225.csv")

out_df_2018 = df_2018[df_2018['US'] <= 10]
out_df_2018[['Artist and Title', 'US']].plot()

out_df_2017 = df_2017[df_2017['US'] <= 10]
raw_2017 = out_df_2017[['Artist and Title', 'US']].plot()

out_df_2016 = df_2016[df_2016['US'] <= 10]
raw_2016 = out_df_2016[['Artist and Title', 'US']].plot()

out_df_2015 = df_2015[df_2015['US'] <= 10]
raw_2015 = out_df_2015[['Artist and Title', 'US']].plot()

out_df_2014 = df_2014[df_2014['US'] <= 10]
raw_2014 = out_df_2014[['Artist and Title', 'US']].plot()