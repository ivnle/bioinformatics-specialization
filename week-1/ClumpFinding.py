from ComputingFrequencies import ComputingFrequencies
from NumberToPattern import NumberToPattern

def ClumpFinding(Genome: str, k: int, L: int, t: int) -> list:
    FrequentPatterns: list = []
    Clump: list = [0] * (4**k)
    n: int = len(Genome)
    
    i: int
    for i in range(n - L + 1):
        FrequencyArray: list = ComputingFrequencies(Genome[i:i+L], k)
        j: int; freq: int
        for j, freq in enumerate(FrequencyArray):
            if freq >= t:
                Clump[j] = 1
    
    z: int; is_clump: int
    for z, is_clump in enumerate(Clump):
        if is_clump:
            pattern: str = NumberToPattern(z, k)
            FrequentPatterns.append(pattern)

    return FrequentPatterns


