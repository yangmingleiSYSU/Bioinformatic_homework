# IPython log file

import sys
import re
filein = open(sys.argv[1],'r')
seq =''
for i in filein:
    if re.search('^>',i):
        pass
    else:
        seq+=i.strip()
filein.close()
print(seq)     
ORFs = [i[0] for i in re.findall('(ATC.+?(TAA|TAG|TGA))',seq)]
ORFslen = [len(i) for i in ORFs]
MaxLenORF = ORFs[ORFslen.index(max(ORFslen))]
fileout = open("MaxLenORF.fa","w")
fileout.write('>MaxLenORF+\n'+MaxLenORF)
fileout.close()
print('ok')
