import os
import glob

prefix_path = ("C:/Users/mpotd/Documents/GitHub/Python-Sample-codes/Mayur_Python_code/Question/wx_data/")
target_path = open('MissingPrcpData.txt', 'w')
file_array = [f for f in os.listdir(prefix_path) if f.endswith('.txt')]
file_array.sort() # file is sorted list

file_array = [os.path.join(prefix_path, name) for name in file_array]

for filename in file_array:
     log = open(filename, 'r')
     lines = log.read().splitlines()
     row_sets = [[c for c in line.split()] for line in lines]
     count = 0
     for line in row_sets:
          if int(line[1]) != -9999 and int(line[2]) != -9999 and int(line[3]) == -9999:
               count = count + 1
     target_path.write(filename.split('/')[9]+'\t'+str(count)+'\n')
