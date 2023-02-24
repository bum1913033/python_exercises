# define function to bubble sort a given list
def bubble_sort(list):
    # find length of list and assign to variable n
    n = len(list)
    # n = 6 for given example list and first loop will run from 0 to 5 index
    for i in range(0, n):  # runs from 0 to 6
        for j in range(0, n - 1):  # runs from 0 to 5
            print("-----")
            print("comparing:", list[j], "and", list[j + 1])
            print("cards state before latest swap:\t", list)

            # compare preceeding value with following value, if greater than, then swap
            if list[j] > list[j + 1]:
                print("\t<------Swapping!------>")
                list[j], list[j + 1] = list[j + 1], list[j]

            print("cards state on latest swap:\t", list)
    print("<-----DONE----->")


cards = [3, 5, 2, 1, 6, 4]

bubble_sort(cards)
print("cards after bubble sorting:\t", cards)
