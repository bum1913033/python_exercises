# initialize two sets of integers
setx = set([1, 2, 3, 6, 8, 9])
sety = set([3, 6, 8, 7, 2, 5])

# intersection = setx.intersection(sety)
# sorted_intersection = sorted(list(intersection))

# initialize empty set
intersection = set()

# find intersection using for loop and nested if loop
for element in setx:
    if element in sety:
        intersection.add(element)
        
# sort list using sorted()
sorted_intersection = sorted(list(intersection))

# print
print(sorted_intersection)