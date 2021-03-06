from ApproximatePatternCount import ApproximatePatternCount
from NumberToPattern import NumberToPattern
from typing import List
from ReverseComplement import ReverseComplement

def FrequentWordsWithMismatchesAndReverseComplements(text: str, k: int, d: int):
    freq_array: List[str] = [0] * (4**k)
    i: int
    for i in range(len(freq_array)):
        freq_array[i] = ApproximatePatternCount(text, NumberToPattern(i, k), d)
        freq_array[i] += ApproximatePatternCount(text, ReverseComplement(NumberToPattern(i, k)), d)
    max_freq = max(freq_array)

    return [NumberToPattern(j, k) for j, p in enumerate(freq_array) if p == max_freq]
    


    
