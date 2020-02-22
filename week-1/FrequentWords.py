from PatternCount import PatternCount

def FrequentWords(Text: str, k: int) -> list:
    FrequentPatterns: list = []
    Count: list = [None] * (len(Text) - k + 1)
    i: int
    for i in range(len(Text) - k + 1):
        Pattern: str = Text[i:i+k]
        Count[i] = PatternCount(Text, Pattern)
    maxCount: int = max(Count)
    j: int
    for j in range(len(Text) - k + 1):
        if Count[j] == maxCount:
            FrequentPatterns.append(Text[j:j+k])
    return sorted(list(set(FrequentPatterns)))