import csv

def csv_writer(nested_array):
    with open('csv_file.csv', mode='w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for array in nested_array:
            csv_writer.writerow(array)