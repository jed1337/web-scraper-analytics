from csv_writer import csv_writer
from txt_writer import txt_writer

nested_array = [
    ['emp_name', 'dept', 'birth_month'],
    ['John Smith', 'Accounting', 'November'],
    ['Erica Meyers', 'IT', 'March'],
    ['Dan Luigi Tating', 'IT', 'January'],
]

csv_writer(nested_array)
txt_writer(nested_array)