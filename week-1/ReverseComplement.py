import re
from typing import Dict

def ReverseComplement(Pattern: str) -> str:
    # Convert to lowercase
    Pattern = Pattern.upper()
    
    # Check if valid DNA string
    if not re.search(r"^[ATCG]+$", Pattern):
        raise ValueError("Invalid DNA string.")

    # Replace each nucleotide with its complementary nucleotide
    map: Dict[str, str] = {
        'A' : 'T', 
        'C' : 'G', 
        'G' : 'C', 
        'T' : 'A'}
    PatternRC: str = ''
    
    n: str
    for n in Pattern:
        PatternRC += map[n]

    # Reverse the string.
    return PatternRC [::-1]