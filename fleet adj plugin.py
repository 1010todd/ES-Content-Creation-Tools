#Thanks to Terin#3772 whom I've stolen lots of the code from his system distancer.

#Value to add by
fleetmult = .1

file_in = "map systems.txt"
file_read = open(file_in, 'r')
output = open('nn' + file_in, 'w')
full = file_read.readlines()
systemtemp = ""
haveFleet = False
for line in full:
  if (line.startswith("system")):
      systemtemp += line
      output.write(line)
      haveFleet = False
  elif (line.startswith('\tfleet')) :
      words = line.split()
      fleetvalue = float(words[len(words)-1])
      fleetvalue *= fleetmult
      systemtemp += "\tadd "
      output.write("\tadd ")
      for n in range(len(words)-1):
            systemtemp += words[n] + " "
            output.write(words[n])
            output.write(" ")
      systemtemp += str(round(fleetvalue)) + "\n"
      output.write(str(round(fleetvalue)))
      output.write("\n")
  else :
        pass
        #output.write(line)
file_read.close