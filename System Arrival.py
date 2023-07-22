#Thanks to Terin#3772 whom I've copied lots of the code from his system distance script.

#Value to add by
offset = 50
minimalarrival = 1500.
maximumarrival = 9000.

file_in = "map systems.txt"
file_read = open(file_in, 'r')
output = open('out' + file_in, 'w')
full = file_read.readlines()
outfull = []
arrivalwritecount=0
for line in range(len(full)):
      if (full[line].startswith('system')):
            habitable=0
            belt=0
            arrivalwritten = False
            #outfull.append(full[line])
      if (full[line].startswith('\thabitable')) :
            #pos_base = float(full[line][5:])
            habitableline = line
            habitable = float(full[line][11:])
            outfull.append(full[line])
            #output.write(full[line])
      elif (full[line].startswith("\tbelt")):
            belt = float(full[line][6:].split()[0])
            outfull.append(full[line])
            #output.write(full[line])
      elif(full[line].startswith("\tarrival")): #If there's an existing arrival, remove it.
            pass
      elif(full[line].startswith("\tobject") and arrivalwritten == False):
            arrival = max(minimalarrival, max(habitable+offset,belt+offset))
            arrival = min(maximumarrival, arrival)
            #output.write('\tarrival '+ str(f"{arrival:.2f}")+'\n') 
            arrivalwritten = True
            #Insert arrival to correct pos+(arrivalwritecount)
            outfull.insert(habitableline-1,'\tarrival '+ str(f"{arrival:.2f}")+'\n')
            arrivalwritecount+=1
            #output.write('\tarrival '+ str(f"{arrival:.2f}")+'\n')
            #output.write(full[line])
            outfull.append(full[line])
      else :
            outfull.append(full[line])
            #output.write(full[line])
output.writelines(outfull)
file_read.close()
output.close()
print("Done!")
input()
