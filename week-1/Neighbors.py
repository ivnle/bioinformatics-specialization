from typing import List
from HammingDistance import HammingDistance

def Neighbors(Pattern: str, d: int) -> List[str]:
    if d == 0:
        return [Pattern]
    if len(Pattern) == 1:
        return [n for n in 'ACGT']
    SuffixNeighborhood: List[str] = Neighbors(Pattern[1:], d)
    Neighborhood: List[str] = []
    p: str
    for p in SuffixNeighborhood:
        if HammingDistance(p, Pattern[1:]) < d:
            Neighborhood += [n + p for n in 'ACTG']
        else:
            Neighborhood += [Pattern[0] + p]
    return Neighborhood


    