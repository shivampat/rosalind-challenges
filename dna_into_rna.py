s = [char for char in input('Enter nucleotide:')]
bases = {
    'a': 0,
    'c': 0,
    'g': 0,
    't': 0
    }  
transcription = s
for letter, i in zip(s, range(len(s))):
    if letter == 'T':
        transcription[i] = 'U'

print('\n\n\n')
print("".join(transcription))