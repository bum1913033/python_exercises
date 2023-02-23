# Given an unsorted array of size N, use selection sort to sort arr[] in increasing order.

my_list = [4, 1, 3, 9, 7]
print("initial:", my_list)

# n = 5
n = len(my_list)

# output: 1 3 4 7 9

# define selection sort function
def selection_sort(my_list, n):
    for i in range(n):
        # assign min index for this iteration, i is the selector.
        min_index = i
        # j is the index after i, used to compare if preceeding element is less than the following element.
        for j in range(i + 1, n):
            if my_list[j] < my_list[min_index]:
                min_index = j
        # swap
        (my_list[i], my_list[min_index]) = (my_list[min_index], my_list[i])
        # print at each iteration
        print("update:\t", my_list)
    # return statement
    return my_list


# final
print("sorted:\t", selection_sort(my_list, n))
