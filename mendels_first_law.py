import numpy as np

populationData = {
    'AA': int(input('Enter k: ')),
    'Aa': int(input('Enter m: ')),
    'aa': int(input('Enter n: ')),
}

# AA AA
# Aa Aa
# aa aa

# removing AA, 3/5
# removing Aa, 3/5
# removing aa, 4/5

population = populationData['AA']+populationData['Aa']+populationData['aa']

firstPick = []
secondPicks = [[],[],[]]
domProbabilities = [[1.0,1.0,1.0],[1.0,.75, .5],[1, .5, 0]]

finalProbability = float(0)

firstPick.append(populationData['AA']/population)
firstPick.append(populationData['Aa']/population)
firstPick.append(populationData['aa']/population)

minus = [[-1, 0, 0],[0, -1, 0],[0, 0, -1]]

i = 0 
for allele in populationData:
    alleles = ['AA', 'Aa', 'aa']
    alleles.remove(allele)
    tempSecond = []
    secondPicks[i].append((populationData['AA']+minus[i][0])/(population-1))
    secondPicks[i].append((populationData['Aa']+minus[i][1])/(population-1))
    secondPicks[i].append((populationData['aa']+minus[i][2])/(population-1))
    i += 1 

secondPicks = np.array(secondPicks)

for k in range(3):
    #tempFin = []
    for i in range(3):
        finalProbability += secondPicks[k][i] * domProbabilities[k][i] * firstPick[k]
    

#print(firstPick)
#print(secondPicks)
print(finalProbability)

#firstPick_AA = (populationData['AA'])/population
#firstPick_Aa = (populationData['Aa'])/population
#firstPick_aa = (populationData['aa'])/population

#22 26 27
