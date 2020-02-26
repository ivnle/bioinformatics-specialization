from MinimumSkew import MinimumSkew
from FrequentWordsWithMismatchesAndReverseComplements import FrequentWordsWithMismatchesAndReverseComplements

with open(r'datasets/Salmonella_enterica.txt', 'r') as f:
    lines = f.readlines()
    g = ''.join([line.strip() for line in lines[1:]])

ms = MinimumSkew(g)
print(ms)
#[3764856, 3764858]

text = g[ms[0] - 425: ms[0] + 425]
print(text)

k = 9
d = 1
fw = FrequentWordsWithMismatchesAndReverseComplements(text, k, d)
print(fw)
# [('TGTGGATAA', 6), ('TTATCCACA', 6)]

