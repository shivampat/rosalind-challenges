file = open('Rosalind Challenges\input files\gc_content.txt')
dna_strings = file.read().replace('\n','')
file.close()
dna_strings_seperated = dna_strings.split('>')[1:]

data = []

for string in dna_strings_seperated: 
    id = string[0:13]
    strand = string[13::]
    cg_count = 0 
    letterCount = len(strand)
    for letter in strand:
        if letter == 'C' or letter == 'G':
            cg_count += 1
    data.append([id,(cg_count/letterCount)])

maxId = data[0][0]
maxPctg = data[0][1]

for strand_data in data: 
    if(strand_data[1] > maxPctg):
        maxId = strand_data[0]
        maxPctg = strand_data[1]

print(maxId)
print(maxPctg*100)
