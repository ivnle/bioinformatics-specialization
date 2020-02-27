k = 9
total_kmers = 4**k
strings_count = 500
string_len = 1000
kmers_in_string = string_len - k + 1
result = strings_count * kmers_in_string / total_kmers
print(result)