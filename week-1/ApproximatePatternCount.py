from HammingDistance import HammingDistance

def ApproximatePatternCount(Text: str, Pattern: str, d: int) -> int:
    count: int = 0
    k: int = len(Pattern)
    i: int
    for i in range(len(Text) - k + 1):
        if HammingDistance(Text[i:i+k], Pattern) <= d:
            count += 1
    return count  
    