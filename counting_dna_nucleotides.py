s = input('Enter nucleotide:')
bases = {
    'a': 0,
    'c': 0,
    'g': 0,
    't': 0
    }   
for letter in s: 
    bases[letter.lower()] += 1

count = f"{bases['a']} {bases['c']} {bases['g']} {bases['t']}"
print(count)