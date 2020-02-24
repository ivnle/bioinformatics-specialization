from PatternToNumberRecursive import PatternToNumberRecursive
from NumberToPatternRecursive import NumberToPatternRecursive

def FindingFrequentWordsBySorting(Text: str, k: int) -> list:
    FrequentPatterns: list = []
    Index: list = []
    Count: list = []
    i:int
    for i in range(len(Text) - k + 1):
        Pattern: str = Text[i:i+k]
        Index.append(PatternToNumberRecursive(Pattern))
        Count.append(1)
    SortedIndex: list = sorted(Index)
    for i in range(1, len(SortedIndex)):
        if SortedIndex[i] == SortedIndex[i-1]:
            Count[i] = Count[i-1] + 1
    maxCount = max(Count)
    for i, j in enumerate(Count):
        if j == maxCount:
            FrequentPatterns.append(NumberToPatternRecursive(SortedIndex[i], k))
    return FrequentPatterns