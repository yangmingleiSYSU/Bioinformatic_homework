# IPython log file
orf = "ATGAGTGTGGATCCAGCTTGTCCCCAAAGCTTGCCTTGCTTTGAAGCATCCGACTGTAAAGAATCTTCACCTATGCCTGTGATTTGTGGGCCTGAAGAAAACTATCCATCCTTGCAAATGTCTTCTGCTGAGATGCCTCACACGGAGACTGTCTCTCCTCTTCCTTCCTCCATGGATCTGCTTATTCAGGACAGCCCTGATTCTTCCACCAGTCCCAAAGGCAAACAACCCACTTCTGCAGAGAAGAGTGTCGCAAAAAAGGAAGACAAGGTCCCGGTCAAGAAACAGAAGACCAGAACTGTGTTCTCTTCCACCCAGCTGTGTGTACTCAATGATAGATTTCAGAGACAGAAATACCTCAGCCTCCAGCAGATGCAAGAACTCTCCAACATCCTGAACCTCAGCTACAAACAGGTGAAGACCTGGTTCCAGAACCAGAGAATGAAATCTAAGAGGTGGCAGAAAAACAACTGGCCGAAGAATAGCAATGGTGTGACGCAGGGATGCCTGGTGAACCCGACTGGGAACCTTCCAATGTGGAGCAACCAGACCTGGAACAATTCAACCTGGAGCAACCAGACCCAGAACATCCAGTCCTGGAGCAACCACTCCTGGAACACTCAGACCTGGTGCACCCAATCCTGGAACAATCAGGCCTGGAACAGTCCCTTCTATAACTGTGGAGAGGAATCTCTGCAGTCCTGCATGCAGTTCCAGCCAAATTCTCCTGCCAGTGACTTGGAGGCTGCCTTGGAAGCTGCTGGGGAAGGCCTTAATGTAATACAGCAGACCACTAGGTATTTTAGTACTCCACAAACCATGGATTTATTCCTAAACTACTCCATGAACATGCAACCTGAAGACGTGTGA"
def translate(ORFseq):
    import re
    codon_dic={'GCU':'A','GCC':'A','GCA':'A','GCG':'A',
           'CGU':'R','CGC':'R','CGA':'R','CGG':'R','AGA':'R','AGG':'R',
           'AAU':'N','AAC':'N',
           'GAU':'D','GAC':'D',
           'UGU':'C','UGC':'C',
           'GAA':'E','GAG':'E',
           'CAA':'Q','CAG':'Q',
           'GGU':'G','GGC':'G','GGA':'G','GGG':'G',
           'CAU':'H','CAC':'H',
           'AUU':'I','AUC':'I','AUA':'I',
           'UUA':'L','UUG':'L','CUU':'L','CUC':'L','CUA':'L','CUG':'L',
           'AAA':'K','AAG':'K',
           'AUG':'M',
           'UUU':'F','UUC':'F',
           'CCU':'P','CCC':'P','CCA':'P','CCG':'P',
           'UCU':'S','UCC':'S','UCA':'S','UCG':'S','AGU':'S','AGC':'S',
           'ACU':'T','ACC':'T','ACA':'T','ACG':'T',
           'UGG':'W','UAU':'Y','UAC':'Y',
           'GUU':'V','GUC':'V','GUA':'V','GUG':'V',
           'UAG':'STOP','UGA':'STOP','UAA':'STOP'}
    if re.search('T',ORFseq):
        ORFseq = re.sub('T','U',ORFseq)
    def trans(ORFseq):
        AAseq = ""
        for i in range(0,len(ORFseq),3):
            AAseq += codon_dic[ORFseq[i:i+3]]
        return AAseq
    AAseq = trans(ORFseq)
    AAseq=re.sub("STOP","*",AAseq)
    return AAseq 
translate(orf)
