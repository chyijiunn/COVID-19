import re
genome_File = open('genome','r')
genomeWithoutBreakFile = open('genomeWithoutBreak','w')

lines = genome_File.readlines()
a=''
for line in lines:
    a += line.strip()
b = a.split()
c = ''.join(b)
genomeWithoutBreakFile.write(c)
genome_File.close()
genomeWithoutBreakFile.close()