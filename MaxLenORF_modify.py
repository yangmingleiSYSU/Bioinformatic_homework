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


ATGs=[i.span() for i in re.finditer('(ATG)',seq)]
ORFs=[]
for i in ATGs:
    start=i[0]
    end=i[1]
    print(end)
    while(end < len(seq)):
        if seq[end:(end+3)] == "TGA" or seq[end:(end+3)] == "TAA" or seq[end:(end+3)] == "TAG":
            end+=3
            ORFs.append((seq[start:end],end-start,[start,end]))
            end=len(seq)
        else:
            end+=3
ORFlens=[i[1] for i in ORFs]
ORFseqs=[i[0] for i in ORFs]
MaxLenORF=ORFseqs[ORFlens.index(max(ORFlens))]
fileout = open("MaxLenORF.fa","w")
fileout.write('>MaxLenORF+\n'+MaxLenORF)
fileout.close()
print('ok')
            
            
