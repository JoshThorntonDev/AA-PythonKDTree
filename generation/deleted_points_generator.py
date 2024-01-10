import random

filename = '3.txt'
filename_write = '3_delete.txt'
data_list = []


def random_data_collection(filename_data, filename_write_data, n):
    with open(filename_data, 'r') as file:
        lines = file.read()
        data_list = lines.split('\n')
    with open(filename_write_data, 'w') as output:
        for i in range(0, n):
            random_data_list = random.choice(data_list)
            output.write('%s %s  \n' % ('D', random_data_list))


random_data_collection(filename,filename_write,20000)
