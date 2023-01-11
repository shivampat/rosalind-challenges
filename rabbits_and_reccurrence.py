n = int(input('Enter n: '))
k = int(input('Enter k: '))


def fibbSequence(n, k): 
    seq = [0,1,1]
    for i in range(3, n+1):
        seq.append(k*seq[i-2]+seq[i-1])
    return seq[1:]

print(fibbSequence(n,k)[-1])
