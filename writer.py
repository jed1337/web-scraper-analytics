import csv
import xlsxwriter

def csv_writer(nested_array):
    with open('output/csv_file.csv', mode='w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for array in nested_array:
            csv_writer.writerow(array)

def txt_writer(nested_array):
    with open('output/txt_file.txt', mode='w') as file:
        for array in nested_array:
            file.write('\t'.join(array))
            file.write('\n')

def excel_writer(nested_array):
    book = xlsxwriter.Workbook('output/excel.xlsx')

    worksheet = book.add_worksheet('Sheet1')

    for row_index in range(0, len(nested_array)):
        for col_index in range(0, len(nested_array[row_index])):
            worksheet.write(row_index, col_index, nested_array[row_index][col_index])
    
    book.close()