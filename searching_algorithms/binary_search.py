# Given a sorted array arr[] of n elements, write a function to search a given element x in arr[]
# and return the index of x in the array. Consider array is 0 base index.

# Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval
# in half. The idea of binary search is to use the information that the array is sorted and reduce the
# time complexity to O(Log n).

# create variables
my_list = [10, 20, 30, 50, 60, 80, 110, 130, 140, 170]
x = 110
n = len(my_list)
low = 0
high = n - 1

# define binary search function based on an iterative approach:
def binaryIterative(my_list, x, low, high):
    while low != high:
        mid = int((low + high)/2)
        if x > my_list[mid]:  # x is on the right side
            low = mid + 1
        else:  # x is on the left side
            high = mid
    if my_list[low] == x:
        print("Found At Index", low)
    elif my_list[high] == x:
        print("Found At Index", high)
    else:
        print("Not Found")

# run function
binaryIterative(my_list, x, low, high)

# Output: index at 6
