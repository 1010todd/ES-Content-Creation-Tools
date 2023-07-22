#Thanks to Terin#3772 whom I've stolen lots of the code from his system distancer.

#Value to add by
fleetmult = .1

file_in = "map systems.txt"
file_read = open(file_in, 'r')
output = open('nn' + file_in, 'w')
full = file_read.readlines()
for line in full:
  if (line.startswith('\tfleet')) :
      words = line.split()
      fleetvalue = float(words[len(words)-1])
      fleetvalue *= fleetmult
      output.write("\t")
      for n in range(len(words)-1):
            output.write(words[n])
            output.write(" ")
      output.write(str(round(fleetvalue)))
      output.write("\n")
  else :
        output.write(line)
file_read.close