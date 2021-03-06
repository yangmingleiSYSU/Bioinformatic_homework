# IPython log file
#!--*--coding:utf-8--*--

seq = "TTCATTATAAATCTAGAGACTCCAGGATTTTAACGTTCTGCTGGACTGAGCTGGTTGCCTCATGTTATTATGCAGGCAACTCACTTTATCCCAATTTCTTGATACTTTTCCTTCTGGAGGTCCTATTTCTCTAACATCTTCCAGAAAAGTCTTAAAGCTGCCTTAACCTTTTTTCCAGTCCACCTCTTAAATTTTTTCCTCCTCTTCCTCTATACTAACATGAGTGTGGATCCAGCTTGTCCCCAAAGCTTGCCTTGCTTTGAAGCATCCGACTGTAAAGAATCTTCACCTATGCCTGTGATTTGTGGGCCTGAAGAAAACTATCCATCCTTGCAAATGTCTTCTGCTGAGATGCCTCACACGGAGACTGTCTCTCCTCTTCCTTCCTCCATGGATCTGCTTATTCAGGACAGCCCTGATTCTTCCACCAGTCCCAAAGGCAAACAACCCACTTCTGCAGAGAAGAGTGTCGCAAAAAAGGAAGACAAGGTCCCGGTCAAGAAACAGAAGACCAGAACTGTGTTCTCTTCCACCCAGCTGTGTGTACTCAATGATAGATTTCAGAGACAGAAATACCTCAGCCTCCAGCAGATGCAAGAACTCTCCAACATCCTGAACCTCAGCTACAAACAGGTGAAGACCTGGTTCCAGAACCAGAGAATGAAATCTAAGAGGTGGCAGAAAAACAACTGGCCGAAGAATAGCAATGGTGTGACGCAGGGATGCCTGGTGAACCCGACTGGGAACCTTCCAATGTGGAGCAACCAGACCTGGAACAATTCAACCTGGAGCAACCAGACCCAGAACATCCAGTCCTGGAGCAACCACTCCTGGAACACTCAGACCTGGTGCACCCAATCCTGGAACAATCAGGCCTGGAACAGTCCCTTCTATAACTGTGGAGAGGAATCTCTGCAGTCCTGCATGCAGTTCCAGCCAAATTCTCCTGCCAGTGACTTGGAGGCTGCCTTGGAAGCTGCTGGGGAAGGCCTTAATGTAATACAGCAGACCACTAGGTATTTTAGTACTCCACAAACCATGGATTTATTCCTAAACTACTCCATGAACATGCAACCTGAAGACGTGTGAAGATGAGTGAAACTGATATTACTCAATTTCAGTCTGGACACTGGCTGAATCCTTCCTCTCCCCTCCTCCCATCCCTCATAGGATTTTTCTTGTTTGGAAACCACGTGTTCTGGTTTCCATGATGCCCATCCAGTCAATCTCATGGAGGGTGGAGTATGGTTGGAGCCTAATCAGCGAGGTTTCTTTTTTTTTTTTTTTCCTATTGGATCTTCCTGGAGAAAATACTTTTTTTTTTTTTTTTTTTGAAACGGAGTCTTGCTCTGTCGCCCAGGCTGGAGTGCAGTGGCGCGGTCTTGGCTCACTGCAAGCTCCGTCTCCCGGGTTCACGCCATTCTCCTGCCTCAGCCTCCCGAGCAGCTGGGACTACAGGCGCCCGCCACCTCGCCCGGCTAATATTTTGTATTTTTAGTAGAGACGGGGTTTCACTGTGTTAGCCAGGATGGTCTCGATCTCCTGACCTTGTGATCCACCCGCCTCGGCCTCCCTAACAGCTGGGATTTACAGGCGTGAGCCACCGCGCCCTGCCTAGAAAAGACATTTTAATAACCTTGGCTGCCGTCTCTGGCTATAGATAAGTAGATCTAATACTAGTTTGGATATCTTTAGGGTTTAGAATCTAACCTCAAGAATAAGAAATACAAGTACAAATTGGTGATGAAGATGTATTCGTATTGTTTGGGATTGGGAGGCTTTGCTTATTTTTTAAAAACTATTGAGGTAAAGGGTTAAGCTGTAACATACTTAATTGATTTCTTACCGTTTTTGGCTCTGTTTTGCTATATCCCCTAATTTGTTGGTTGTGCTAATCTTTGTAGAAAGAGGTCTCGTATTTGCTGCATCGTAATGACATGAGTACTGCTTTAGTTGGTTTAAGTTCAAATGAATGAAACAACTATTTTTCCTTTAGTTGATTTTACCCTGATTTCACCGAGTGTTTCAATGAGTAAATATACAGCTTAAACATAA"
import re
ORFs_erro=re.findall('(ATG([TACG]{3})+?(TAA|TAG|TGA))',seq) ###这样直接找是不对的因为正则默认找过的位置就不再找了
ORFs_pos = [(o.span(),o.group()) for o in re.finditer('(ATG([TACG]{3})+?(TAA|TAG|TGA))',seq)]
###此解析查看直接正则表达式找的位置信息和序列信息，发现找到的ORFs位置是没有重叠的，没有考虑到
ATGs=[i.span() for i in re.finditer('(ATG)',seq)]###找到所有起始密码子并返回位置信息
    
orfs = []
for i in ATGs:
    seqlist = [o.group() for o in re.finditer('(ATG([TACG]{3})+?(TAA|TAG|TGA))',seq[i[0]:])]
#从起始密码子所在的位置开始往后找
    print(seqlist[0])
    orfs+=[seqlist[0]] #此处一定要加中括号，每一个起始密码子往后都可能找到很多ORF是，取第一个
    
len(orfs)
