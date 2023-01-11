from textwrap import wrap

codonChart = {
'UUU': 'F',
'UUC': 'F',
'UUA': 'L',
'UUG': 'L',
'UCU': 'S',
'UCC': 'S',
'UCA': 'S',
'UCG': 'S',
'UAU': 'Y',
'UAC': 'Y',
'UAA': 'Stop',
'UAG': 'Stop',
'UGU': 'C',
'UGC': 'C',
'UGA': 'Stop',
'UGG': 'W',
'CUU': 'L',
'CUC': 'L',
'CUA': 'L',
'CUG': 'L',
'CCU': 'P',
'CCC': 'P',
'CCA': 'P',
'CCG': 'P',
'CAU': 'H',
'CAC': 'H',
'CAA': 'Q',
'CAG': 'Q',
'CGU': 'R',
'CGC': 'R',
'CGA': 'R',
'CGG': 'R',
'AUU': 'I',
'AUC': 'I',
'AUA': 'I',
'AUG': 'M',
'ACU': 'T',
'ACC': 'T',
'ACA': 'T',
'ACG': 'T',
'AAU': 'N',
'AAC': 'N',
'AAA': 'K',
'AAG': 'K',
'AGU': 'S',
'AGC': 'S',
'AGA': 'R',
'AGG': 'R',
'GUU': 'V',
'GUC': 'V',
'GUA': 'V',
'GUG': 'V',
'GCU': 'A',
'GCC': 'A',
'GCA': 'A',
'GCG': 'A',
'GAU': 'D',
'GAC': 'D',
'GAA': 'E',
'GAG': 'E',
'GGU': 'G',
'GGC': 'G',
'GGA': 'G',
'GGG': 'G',
}

file = open(r'Rosalind Challenges\input files\rna_into_proteins.txt')
strand = file.read()
file.close()
strand = wrap(strand, 3)

protein = ''

for codon in strand: 
    if codonChart[codon] != 'Stop':
        protein += codonChart[codon]

print(protein)
