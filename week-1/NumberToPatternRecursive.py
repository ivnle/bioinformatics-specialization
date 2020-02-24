from typing import Dict

map: Dict[int, str] = {
    0: 'A', 
    1: 'C', 
    2: 'G', 
    3: 'T'}

def NumberToPatternRecursive(number: int, k: int) -> str:
    if k == 1:
        return map[number]
    return NumberToPatternRecursive(number // 4, k - 1) + NumberToPatternRecursive(number % 4, 1)