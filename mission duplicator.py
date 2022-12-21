
templatefile = "ath template.txt"
outputfile = "ath out.txt"

missionCount = 5

#Alphabets if you want to use one.
az = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
azCap = [a.upper() for a in az]

list1 = ['Arneb', 'Alnilam', 'Mebsuta']
list2 = ['Haven','Zenith','Featherweight']
list3 = [a.casefold() for a in list2]
listnum = [i for i in range(missionCount)] #example of numbered mission duping.

replaceKeys = ['[system]','[planet]','[planetlc]']
replaceWith = [list1,list2,list3]


f = open(templatefile,'r')
filedata = f.read()
f.close()

missionsetlist = []
sep = '\n'

#newdata = filedata

for nn in range(len(list1)):
    newdata = filedata
    for n in range(len(replaceKeys)):
        newdata = newdata.replace(replaceKeys[n],replaceWith[n][nn])
        #print(replaceWith[n][nn])
        #print(replaceKeys[n])
    missionsetlist.append(newdata)
print("Done. Press any key to continue...")
input()
f = open(outputfile,'w')
f.write(sep.join(missionsetlist))
f.close()