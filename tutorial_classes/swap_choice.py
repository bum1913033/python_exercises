# given list -> swap position of two elements whose indices are given

# create a list of numbers
numlist = [1,2,3,4,5]
size = numlist.__len__()
# take pos1 and pos2 from user
pos1 = int(input("Enter pos1:\t"))
pos2 = int(input("Enter pos2:\t"))

# define a function to swap pos1 and pos2
def swapper(numlist, pos1, pos2):
    # if pos1 < 0 assign index 0
    if pos1 <= 0:
        pos1 == 0
    # else pos1 = pos1 -1
    else:
        pos1 = pos1 -1
    
    # if pos2 > list[last]
    if pos2 >= size:
        pos2 = size-1
        print("is this working?", pos2)
    
    # test print
    print(numlist[pos1])
    print(numlist[pos2])

    # create temp variables to store popped elements
    first_ele = numlist.pop(pos1)
    second_ele = numlist.pop(pos2-1)
    
    # insert into swapped positions
    numlist.insert(pos1, second_ele)
    numlist.insert(pos2, first_ele)
    
    # return list
    return numlist

# print
print(swapper(numlist, pos1, pos2))