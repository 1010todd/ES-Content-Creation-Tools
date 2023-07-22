#=================
#Config:
small_fleet_min = 850
small_fleet_max = 1650
small_fleet_mult = 1

large_fleet_min = 2000
large_fleet_max = 4000
large_fleet_mult = 1

#Note even number on the list will be placed as large fleet.
fleet_list = [
    "Small Southern Merchant",
    "Large Southern Merchant"
]

#=================

import random
import math
#random.seed(3457023)

def roundup1000(x):
    return int(math.ceil(x / 1000.0)) * 1000
def roundup100(x):
    return int(math.ceil(x / 100.0)) * 100
def roundup10(x):
    return int(math.ceil(x / 10.0)) * 10
def roundup5(x):
    return int(math.ceil(x / 5.0)) * 5

def randomizeFleet(add):
      return add + ' ' + str(roundup100(random.randrange(small_fleet_min,small_fleet_max)*small_fleet_mult)) + '\n'
def randomizeFleetLarge(add):
      return add + ' ' + str(roundup100(random.randrange(large_fleet_min,large_fleet_max)*large_fleet_mult)) + '\n'

linesToAdd = []

for fleet in fleet_list:
    linesToAdd.append(f'\tadd fleet "{fleet}"')
    
#linesToAdd = ['\tadd fleet "Small Southern Merchant"']

file_in = "map systems.txt"
file_read = open(file_in, 'r')
output = open('outfleet ' + file_in, 'w')
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
      if (True):
        for n in range(len(linesToAdd)):
            if (full[line].startswith('\tattributes "dirt belt"')):
                  #outfull.append(full[line])
                  if (n % 2 == 0):
                    buffer.append(randomizeFleet(linesToAdd[n]))
                  else:
                    buffer.append(randomizeFleetLarge(linesToAdd[n]))
                  written = True
            elif (full[line].startswith('\tattributes "rim"')):
                  #outfull.append(full[line])
                  if (n % 2 == 0):
                    buffer.append(randomizeFleet(linesToAdd[n]))
                  else:
                    buffer.append(randomizeFleetLarge(linesToAdd[n]))
                  written = True
            elif (full[line].startswith('\tattributes "south"')):
                  #outfull.append(full[line])
                  if (n % 2 == 0):
                    buffer.append(randomizeFleet(linesToAdd[n]))
                  else:
                    buffer.append(randomizeFleetLarge(linesToAdd[n]))
                  written = True
            elif (full[line].startswith('\tattributes "nan"')):
                  #outfull.append(full[line])
                  if (n % 2 == 0):
                    buffer.append(randomizeFleet(linesToAdd[n]))
                  else:
                    buffer.append(randomizeFleetLarge(linesToAdd[n]))
                  written = True
            else :
                  #outfull.append(full[line])
                  pass
      if (False):
        for stuff in linesToAdd:
            if (full[line].startswith('\tattributes "dirt belt"')):
                  #outfull.append(full[line])
                  buffer.append(randomizeFleet(stuff))
                  written = True
            elif (full[line].startswith('\tattributes "rim"')):
                  #outfull.append(full[line])
                  buffer.append(randomizeFleet(stuff))
                  written = True
            elif (full[line].startswith('\tattributes "south"')):
                  #outfull.append(full[line])
                  buffer.append(randomizeFleet(stuff))
                  written = True
            else :
                  #outfull.append(full[line])
                  pass
            #output.write(full[line])
output.writelines(outfull)
file_read.close