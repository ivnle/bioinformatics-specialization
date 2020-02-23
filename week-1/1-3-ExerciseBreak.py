from PatternMatching import PatternMatching

pattern = "CTTGATCAT"
with open('Vibrio_cholerae.txt', 'r') as file:
    genome = file.read()

print(*PatternMatching(pattern, genome),sep=' ')