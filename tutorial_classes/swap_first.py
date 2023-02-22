# create list
input_list = [12, 35, 9, 56, 24]

# define function to swap first and last element of list
def swapFirst(input_list):
    # size = length of list
    size = input_list.__len__()
    # temp variable = first index
    temp = input_list[0]
    # input_list[first index] = input_list[last index]
    input_list[0] = input_list[size - 1]
    # input_list[last index] = temp variable
    input_list[size - 1] = temp
    return input_list

print(input_list)
print(swapFirst(input_list))