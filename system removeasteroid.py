#Thanks to Terin#3772 whom I've copied lots of the code from his system distance script.

import random

random.seed(3457023)

file_in = "map.txt"
file_read = open(file_in, 'r')
output = open('map_noroid.txt', 'w')
full = file_read.readlines()
outfull = []
arrivalwritecount=0
buffer = []
written = False
for line in range(len(full)):
      if (full[line].startswith('\tasteroids')):
            pass
      else :
            outfull.append(full[line])
            pass
            #output.write(full[line])
output.writelines(outfull)
file_read.close