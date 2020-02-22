from typing import Dict

def NumberToPattern(index: int, k: int) -> str:

    map: Dict[int, str] = {
        0: 'A', 
        1: 'C', 
        2: 'G', 
        3: 'T'}
    b: int = 4**(k-1)
    if (index // b) > 3:
        raise ValueError('index is greater than the max value of k digits in base 4')    
    pattern: str = ''
    i: int
    for i in range(k):
        pattern += map[index // b]
        index %= b
        b //= 4
    return pattern

