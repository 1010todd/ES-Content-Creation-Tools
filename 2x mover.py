import os

movefrom = input("Move from: ")
moveto = input("Move to: ")

#shiplist = os.listdir("ship/")
filelist = os.listdir(f"{movefrom}/")
x2list = []
for file in filelist:
    if file.endswith("@2x.png"):
        x2list.append(file)
#print(x2list)
for filename in x2list:
    os.rename(f"{movefrom}/{filename}",f"{moveto}\{filename}")