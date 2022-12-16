from itertools import combinations_with_replacement
#https://www.geeksforgeeks.org/permutation-and-combination-in-python/

varieties = ['Chocolate' , 'Glazed' , 'Strawberry']

print(f"Our varieties are: {varieties}")


donut_combinations = combinations_with_replacement(varieties, 6)

index = 0
for i in list(donut_combinations):
    index += 1
    print(f'# {index}: ', end = '')
    print (i)