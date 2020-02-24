from ClumpFinding import ClumpFinding

k = 9
L = 500
t = 3

with open('E_coli.txt', 'r') as file:
    genome = file.read()

print(len(ClumpFinding(genome, k, L, t)))