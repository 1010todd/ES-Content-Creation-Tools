#Thanks to Terin#3772 whom I've stolen lots of the code from his system distancer.

import os


dirlist = os.listdir()

for afile in dirlist:
      afile = afile.casefold()
      if afile.endswith(".txt") and afile.find('ship') != -1 and not afile.startswith('errorreport'):
            file_in = afile
            file_read = open(file_in, 'r')
            output = open(f'errorreport{file_in}.txt', 'w')
            full = file_read.readlines()
            checkstart = False
            checkpass = False
            isVariant = False
            shipname = ''
            i = 0
            for line in full:
                  i += 1
                  linesplit = line.split('#')
                  line = linesplit[0]
                  if (line.startswith('outfit')):
                        checkstart = False
                  elif (line.startswith('ship')) :
                        if (shipname == ''):
                              pass
                        elif (not checkpass and not isVariant):
                              output.write(f'\nship {shipname} at line {shipline} has no drag!')
                        shipname = line[5:]
                        shipline = i
                        checkstart = True
                        checkpass = False
                        isVariant = False
                        if line.count('"') >= 4 or line.count('`') >= 4:
                              isVariant = True
                        #output.write(line)
                  elif isVariant and line.find('attributes') >= 1 and (line.find('add') < 1):
                        isVariant = False
                  elif (line.find('drag') != -1 and checkstart and not isVariant) :
                        value = line.split()
                        if float(value[1]) > 0.:
                              checkpass = True
                        #output.write('\n')
file_read.close()
output.close()