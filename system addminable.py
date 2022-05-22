#Thanks to Terin#3772 whom I've copied lots of the code from his system distance script.

import random

random.seed(3457023)

def randomizeRoids(add):
      return add + ' ' + str(random.randrange(1,30)) + ' ' + str(abs(random.gauss(2,1))) + '\n'

linesToAdd = []

linetoadd = '\tadd minables "mega rock"'
addhugerock1 = '\tadd minables "huge rock"'
addhugeice1 = '\tadd minables "huge ice"'
addhugeiron1 = '\tadd minables "huge iron"'
addlargesilicon1 = '\tadd minables "large silicon"'
addhugelead1 = '\tadd minables "huge lead"'
addlargecopper1 = '\tadd minables "large copper"'

file_in = "map.txt"
file_read = open(file_in, 'r')
output = open('outroid' + file_in, 'w')
full = file_read.readlines()
outfull = []
arrivalwritecount=0
buffer = []
written = False
for line in range(len(full)):
      if (full[line].startswith('system')):
            if written == True:
                  outfull.extend(buffer)
            buffer.clear()
            #outfull.append(full[line])
            buffer.append(full[line])
            written = False
            if (random.random() >= 0.5):
                  buffer.append(randomizeRoids(addhugerock1))
                  written = True
            if (random.random() >= 0.7):
                  buffer.append(randomizeRoids(addhugeice1))
                  written = True
      if (full[line].startswith('\tasteroids "large metal"')):
            #outfull.append(full[line])
            buffer.append(randomizeRoids(linetoadd))
            written = True
      elif (full[line].startswith('\tminables iron')):
            #outfull.append(full[line])
            buffer.append(randomizeRoids(addhugeiron1))
            written = True
      elif (full[line].startswith('\tminables silicon')):
            #outfull.append(full[line])
            buffer.append(randomizeRoids(addlargesilicon1))
            written = True
      elif (full[line].startswith('\tminables lead')):
            #outfull.append(full[line])
            buffer.append(randomizeRoids(addhugelead1))
            written = True
      elif (full[line].startswith('\tminables copper')):
            #outfull.append(full[line])
            buffer.append(randomizeRoids(addlargecopper1))
            written = True
      else :
            #outfull.append(full[line])
            pass
            #output.write(full[line])
output.writelines(outfull)
file_read.close