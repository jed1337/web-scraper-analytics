from writer import csv_writer, txt_writer, excel_writer

nested_array = [
    ['emp_name', 'dept', 'birth_month'],
    ['John Smith', 'Accounting', 'November'],
    ['Erica Meyers', 'IT', 'March'],
    ['Dan Luigi Tating', 'IT', 'January'],
]

csv_writer(nested_array)
txt_writer(nested_array)
excel_writer(nested_array)