from ComputingFrequencies import ComputingFrequencies
from NumberToPattern import NumberToPattern

def FasterFrequentWords(Text: str, k: int) -> list:
    FrequentPatterns: list = []
    FrequencyArray: list = ComputingFrequencies(Text, k)
    maxCount: int = max(FrequencyArray)
    
    i: int
    for i in range(len(FrequencyArray)):
        if FrequencyArray[i] == maxCount:
            Pattern: str = NumberToPattern(i, k)
            FrequentPatterns.append(Pattern)
    return list(set(FrequentPatterns))
    