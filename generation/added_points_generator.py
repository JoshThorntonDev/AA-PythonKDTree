import random
import math
import sys

category = ['restaurant', 'education', 'hospital']
latitude = 88.3021951926
longitude = 132.7535258216
filename = 'addingpoints/100000/addTo3.in'
num = 20000

def random_data_generator(lat, lon, cat, n, file_n):
    with open(file_n, 'w') as output:
        for i in range(1, n):
            id = 'id' + str(i*200000)
            random_cat = random.choice(cat)
            dec_lat = random.random() / 100
            dec_lon = random.random() / 100
            output.write('%s %s %s %.10f %.10f \n' % ('A',id, random_cat, lat + dec_lat, lon + dec_lon))


random_data_generator(latitude, longitude, category, num, filename)