import random
import math
import sys

category = ['restaurant', 'education', 'hospital']
latitude = 12.3251846958
longitude = 3.2514758496
filename = '10.txt'
num = 500

def random_data_generator(lat, lon, cat, n, file_n):
    with open(file_n, 'w') as output:
        for i in range(0, n):
            id = 'id' + str(i)
            random_cat = random.choice(cat)
            dec_lat = random.random() / 100
            dec_lon = random.random() / 100
            output.write('%s %s %.10f %.10f \n' % (id, random_cat, lat + dec_lat, lon + dec_lon))


random_data_generator(latitude, longitude, category, num, filename)
