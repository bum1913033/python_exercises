# Algorithm
# Set the first element as selector (current element)
# If selector is the target element, return index
# If not and if more elements in list, set selector to the following element and repeat step 2
# If no more elements in list, then return -1 to indicate that the element was not found

# define function to search sequentially over a list
def linear_search(my_list, n, target_element):
    # i is the selector index
    for i in range(n):
        # if selected index == target element then:
        if my_list[i] == target_element:
            # return index of selected index
            return i
    # if not found after looping over the list, then return -1
    return -1


# variables
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(my_list)
target_element = 9

# store result of calling function to result variable
result = linear_search(my_list, n, target_element)

# if result == -1 then target was not found
if result == -1:
    print("search target was not found in the list")
else:
    print("the search target is at index:", result)
