import random

# initialize list
numbers_list = []

#function
def even_num(n):
    if (n % 2) == 0:
        return True

# add 20 random numbers to list
for i in range(0,20):
    numbers_list.append(random.randint(1, 100))

# check whether list element is even or odd
for i in range(0,20):
    if even_num(numbers_list[i]) == True:
        print(f'{numbers_list[i]} is even!')
    else:
        print(f'{numbers_list[i]} is odd!')