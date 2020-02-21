from typing import Dict

def PatternToNumber(Pattern: str) -> int:
    k: int = len(Pattern)
    
    map: Dict[str, int] = {'A': 0, 
                           'C': 1, 
                           'G': 2, 
                           'T': 3}
    
    Number:int = 0
    
    n: str
    for n in Pattern:
        Number += map[n] * (4**(k-1))
        k -= 1
    
    return Number

Pattern: str = 'GT' 
print(PatternToNumber(Pattern)) # 11

Pattern: str = 'ATGCAA' 
print(PatternToNumber(Pattern)) # 912