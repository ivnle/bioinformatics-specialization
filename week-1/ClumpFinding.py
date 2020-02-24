from ComputingFrequencies import ComputingFrequencies
from NumberToPattern import NumberToPattern
from PatternToNumber import PatternToNumber

def ClumpFinding(Genome: str, k: int, L: int, t: int) -> list:
    FrequentPatterns: list = []
    Clump: list = [0] * (4**k)
    n: int = len(Genome)
    FrequencyArray: list = ComputingFrequencies(Genome[:L], k)
    i: int; freq: int
    for i, freq in enumerate(FrequencyArray):
        if freq >= t:
            Clump[i] = 1
    
    j: int
    for j in range(1, n - L + 1):
        
        FirstPattern = Genome[j-1:j-1+k]
        index = PatternToNumber(FirstPattern)
        if FrequencyArray[index] > 0:
            FrequencyArray[index] -= 1
        
        LastPattern = Genome[j+L-k:j+L]
        index = PatternToNumber(LastPattern)
        FrequencyArray[index] += 1        
        if FrequencyArray[index] >= t:
            Clump[index] = 1
    
    z: int; is_clump: int
    for z, is_clump in enumerate(Clump):
        if is_clump:
            pattern: str = NumberToPattern(z, k)
            FrequentPatterns.append(pattern)

    return FrequentPatterns


