population_nums = input('Enter nums: ').split(' ')
for i, num in enumerate(population_nums):
    population_nums[i] = int(num)

offspring_population_nums = []

probabilities = [1, 1, 1, .75, .5, 0]

for num, probability in zip(population_nums, probabilities):
    offspring_population_nums.append(num*2*probability)

print(sum(offspring_population_nums))
