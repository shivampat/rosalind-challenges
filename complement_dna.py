s = input('Enter sequence: ')

bases = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A',
    }  

reverse_complement = []
for base in s[::-1]: 
    reverse_complement.append(bases[base])

print('\n\n\n',''.join(reverse_complement))