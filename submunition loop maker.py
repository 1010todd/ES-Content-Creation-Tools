import os
# get current working directory
cwd = os.getcwd()
#get files in directory
files = os.listdir(cwd) 

print(files)

file_name = input("Enter filename(with type): ")
loop_count = int(input("Loop count: "))

def listToString(s): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(s))

def writeBatch(loop_count):
    ii = 0
    loopnum = 1
    while loop_count > 0:
        
        for line in full:
            ii += 1
            
            if line.startswith("outfit"):
                a = line.split()
                indexed_replace = a.index("[replace]")
                a[indexed_replace] = str(loopnum)
                output.write(listToString(a))
                output.write("\n")
                print(listToString(a))
            elif line.startswith("\t\tsubmunition"):
                b = line.split()
                try:
                    indexed_replace = b.index("[replace]")
                except:
                    output.write(line)
                else:
                    #indexed_replace = b.index("[replace]")
                    b[indexed_replace] = str(loopnum+1)
                    output.write("\t\t")
                    output.write(listToString(b))
                    output.write("\n")
                    print(listToString(b))
            else:
                output.write(line)
        loopnum += 1
        loop_count -= 1
        output.write("\n")

file_in = open(file_name, 'r')
#file_read = open(file_in, 'r')
full = file_in.readlines()
output = open(file_name + "out", 'w')
i = loop_count
writeBatch(loop_count)
    
file_in.close
output.close
input("Press any key to continue")