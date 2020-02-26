from typing import List
from HammingDistance import HammingDistance

def ApproximatePatternMatching(Text: str, Pattern: str, d: int) -> list:
    positions: List[int] = []
    k: int = len(Pattern)
    i: int
    for i in range(len(Text) - k + 1):
        if HammingDistance(Text[i:i+k], Pattern) <= d:
            positions.append(i)
    return positions