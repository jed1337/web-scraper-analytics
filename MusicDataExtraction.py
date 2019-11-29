from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
import os
import glob

def scrape(url, i):
        html = requests.get(url).content
        df_list = pd.read_html(html)
        df = df_list[-1]
        filename = '20' + str(i) + '1225_in'
        df.to_csv(filename + '.csv')
        i_csv = '20' + str(i) + '1225_in.csv'
        o_csv = '20' + str(i) + '1225.csv'
        u_csv = '20' + str(i) + '1225_out.csv'
        e_csv = '20' + str(i) + '1225_e.csv'
        remove_x_row(i_csv, o_csv)
        rename_col_zero(o_csv, u_csv, i)
        remove_first_row(u_csv, e_csv)
        merge_files()
        remove_first_row('consolidated_1.csv', 'consilidated.csv')
        
def remove_x_row(i_csv, o_csv):
        row_count = 0
        cols_to_remove = []
        if i_csv == '20161225_in.csv' or i_csv == '20171225_in.csv' or i_csv == '20181225_in.csv':
                cols_to_remove.append(5)     
        with open(i_csv, "r", encoding="utf8") as source:
                reader = csv.reader(source)
                with open(o_csv, "w", newline='', encoding="utf8") as result:
                    writer = csv.writer(result)
                    for row in reader:
                        row_count += 1
                        for col_index in cols_to_remove:
                            del row[col_index]
                        writer.writerow(row)

def rename_col_zero(o_csv, u_csv, i):
        wine = pd.read_csv(o_csv)
        wine['Unnamed: 0'] = '20'+str(i)
        wine.rename(columns={'Unnamed: 0':'Year'}, inplace=True)
        wine.to_csv(u_csv)

def remove_first_row(i_csv, o_csv):
        row_count = 0
        cols_to_remove = [0]  
        with open(i_csv, "r", encoding="utf8") as source:
                reader = csv.reader(source)
                with open(o_csv, "w", newline='', encoding="utf8") as result:
                    writer = csv.writer(result)
                    for row in reader:
                        row_count += 1
                        for col_index in cols_to_remove:
                            del row[col_index]
                        writer.writerow(row)
def merge_files():
        li = []
        path = os.path.dirname(os.path.abspath(__file__))
        all_files = glob.glob(os.path.join(path, "*_e.csv"))

        df_from_each_file = (pd.read_csv(f) for f in all_files)
        concatenated_df   = pd.concat(df_from_each_file, ignore_index=True, sort=False)
        concatenated_df.to_csv('consolidated_1.csv')

def delete_other_csv():
        for i in range(14,19):
                os.remove('20' + str(i) + '1225.csv')
                os.remove('20' + str(i) + '1225_out.csv')
                os.remove('20' + str(i) + '1225_in.csv')
                os.remove('20' + str(i) + '1225_e.csv')
        os.remove('consolidated_1.csv')

def extract():
        for i in range(14,19):
           scrape ('https://kworb.net/ww/archive/20' + str(i) + '1225.html', i)
           
        delete_other_csv()


extract()   
