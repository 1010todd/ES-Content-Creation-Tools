#Thanks to Terin#3772 whom I've copied lots of the code from his system distance script.

#Value to add by
#x_move = +3000.
#y_move = 0.

x_move = int(input("X offset: "))
y_move = int(input("Y offset: "))

file_in = "map systems.txt"
file_read = open(file_in, 'r')
output = open('n' + file_in, 'w')
full = file_read.readlines()
for line in full:
  if (line.startswith('\tpos')) :
        #pos_base = float(line[5:])
        pos_start = line[5:]
        pos_one, pos_two = pos_start.split()
        npos_one = float(pos_one) + x_move
        npos_two = float(pos_two) + y_move
        output.write('\tpos ' + str(round(npos_one,2)) + ' ' + str(round(npos_two,2)) + "\n")
  else :
        output.write(line)
file_read.close