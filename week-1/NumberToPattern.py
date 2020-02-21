def NumberToPattern(index, k):
    map = {'0': 'A', 
           '1': 'C', 
           '2': 'G', 
           '3': 'T'}
    output_string = ''
    b = 4**(k-1)
    while index > 0:
        output_string += map[str(index // b)]
        index %= b
        b //= 4
    return output_string

index = 5437
k = 7
print(NumberToPattern(index, k))

index = 5437
k = 8
print(NumberToPattern(index, k))
        

