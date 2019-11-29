def txt_writer(nested_array):
    with open('txt_file.txt', mode='w') as file:
        for array in nested_array:
            file.write('\t'.join(array))
            file.write('\n')