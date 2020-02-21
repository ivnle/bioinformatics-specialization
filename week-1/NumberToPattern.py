def NumberToPattern(index, k):
    output_string = ''
    b = 4**(k-1)
    while index > 0:
        output_string += str(index // b)
        index %= b
        b //= 4
    
    map = {'0': 'A', 
           '1': 'C', 
           '2': 'G', 
           '3': 'T'}
    nstring = ''
    for x in output_string:
        nstring += map[x]
    return nstring

index = 5437
k = 7
print(NumberToPattern(index, k))
        

