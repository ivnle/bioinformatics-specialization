from PatternToNumber import PatternToNumber

def ComputingFrequencies(Text: str, k: int) -> str:
    FrequencyArray = [0] * (4**k)
    
    i: int
    for i in range(len(Text) - k + 1):
        Pattern = Text[i:i+k]
        j = PatternToNumber(Pattern)
        FrequencyArray[j] += 1
    
    return ' '.join(str(x) for x in FrequencyArray)

""" Text: str = 'AGCATATTGAACTCGGAGCTGTAATGTGTTCGCAAACTTGACGACCAGTAACGGGTTCTTGGGATACGCGGTCTAGCGAACCTTGGATACGGTGAGCCCGTGGAGATAGAGCGGACCGGTGCTAAGCTGTATGCAGTCTGCCTTAATTCGAGAGACAGTACTACCACTTGGAACATTACTCGAGGTCATGGTTGGAGCTCAGGCTGGTTTCTCATCACCGGGAGGACGTGGCCGGCGTAGTGTACGTCCGACCACCGGCTAGGCATGCACTCTAGTGGGCTGTACGCCAGGGAACCGGAGTCTTATTCCCCTCATTTTACCGCACAAAATGCTGTCTAACGGGCGCCGTCCCAAGTCACAGTTCGTCCCCGTGCGCGCCCCCAAGTTTAGACCCCATAGCAGGACGGAACGACGCCCGGTATCGAGGGCGCTCCCAGCATAACCAAGATTTATGGGAAACCAGCCCCACAATACAAATCTATCATTTGAGTAGCCAGCAACCAGGATCTCTGGAAAGTTAGGTCTTGTCATGAGACGCTATAGACTACACGATTTTGACGTTTTTCACTTATTTTGCGTACACCTACCAGGTGTTGCAAATGAGTGTGTTAAACTCCTCATTTATCTGTTACAAACCTCGTACCTTACTTAGCATGGGGTCTGCGAGTGCCGTAGCAAGCCTGCTGATGGCGGCGCTTACAAACTGAGGATCACAAAGAGTACCCCGGTCCGCGCCCGAAGTCGGCGGTACCTTGCTAGTCTGTAAGTACCTAATACTCCAAGGGTGTACC' 
k: int = 7
output_file = open('ComputingFrequencies.txt', 'w')
print(ComputingFrequencies(Text, k), file=output_file)
output_file.close() """