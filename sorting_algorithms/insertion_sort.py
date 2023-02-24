# Insertion sort is adaptive in nature, i.e. it is appropriate for data sets which are already partially sorted.

my_list = [12, 11, 13, 5, 6]
n = len(my_list)

# selector key starts from index 1 instead of 0
# selector is compared to index [selector-1]
# if selector < selector-1 then swap
# keep doing until sorted


def insertion_sort(my_list, n):
    for i in range(0, n):
        for j in range(1, n):
            if my_list[j] < my_list[j - 1]:
                (my_list[j], my_list[j - 1]) = (my_list[j - 1], my_list[j])
    return my_list


print(insertion_sort(my_list, n))
