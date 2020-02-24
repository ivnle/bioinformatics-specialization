import re
from typing import Dict

def PatternToNumberRecursive(Pattern: str) -> int:
    n: int = len(Pattern)
    if n == 1:
        map: Dict[str, int] = {
            'A': 0, 
            'C': 1, 
            'G': 2, 
            'T': 3}
        return map[Pattern]
        
    return 4 * PatternToNumberRecursive(Pattern[:-1]) + PatternToNumberRecursive(Pattern[-1])