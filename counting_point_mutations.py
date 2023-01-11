s = input('Enter s: ')
t = input('Enter t: ')

hamming_distance = 0 

for letter_s, letter_t in zip(s,t):
    if letter_s != letter_t: 
        hamming_distance += 1

print(hamming_distance)