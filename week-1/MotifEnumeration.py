from typing import List
from Neighbors import Neighbors
from HammingDistance import HammingDistance
import re

def MotifEnumeration(Dna: List[str], k: int, d:int) -> set:
    Patterns = set()
    for i in range(len(Dna[0]) - k + 1):
        for n in Neighbors(Dna[0][i:i+k], d):
            n_found = 0
            for a in Dna[1:]:
                for j in range(len(a) - k + 1):
                    if HammingDistance(a[j:j+k], n) <= d:
                        n_found += 1
                        break
            if n_found == len(Dna[1:]):
                Patterns.add(n)
    return Patterns

