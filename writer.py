import csv

def csv_writer(nested_array):
    with open('csv_file.csv', mode='w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for array in nested_array:
            csv_writer.writerow(array)

def txt_writer(nested_array):
    with open('txt_file.txt', mode='w') as file:
        for array in nested_array:
            file.write('\t'.join(array))
            file.write('\n')