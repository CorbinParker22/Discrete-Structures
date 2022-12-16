from itertools import combinations_with_replacement
#https://www.geeksforgeeks.org/permutation-and-combination-in-python/

varieties = ['Chocolate' , 'Glazed' , 'Strawberry' , 'Bluebery' , 'Coconut', 'Cinnamon' , 'Maple' , 'Crumb' , 'Sugar' , 'Powder' , 'Fruit Filled' , 'Cream filled',\
                  'Jelly filled', 'Boston Cream' , 'Donut Holes' , 'Cronut' , 'Old Fashioned' , 'Long John Glazed' , 'Long John Chocolate' , 'Long John Strawberry',\
                      'Long John Maple']

print(f"Our varieties are: {varieties}")

#had to lower it to 9 donuts to each combination becasue my computer would not play nice with 12
donut_combinations = combinations_with_replacement(varieties, 9)


index = 0
for i in list(donut_combinations):
    index += 1
    print(f'# {index}: ', end = '')
    print (i)