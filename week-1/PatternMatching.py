def PatternMatching(Pattern: str, Genome: str) -> list:
    k: int = len(Pattern)
    n: int = len(Genome)
    starting_positions: list = []
    i:int
    for i in range(n - k + 1):
        if Genome[i:i+k] == Pattern:
            starting_positions.append(i)
    return starting_positions
    