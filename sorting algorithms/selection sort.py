# import
import random

# create a card variable to store a list of 10 integers
cards = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# randomize the position of integers as if shuffling a deck of cards
random.shuffle(cards)
# print the current state of cards list
print(cards)

# get length of cards list and assign to deck_size variable
deck_size = cards.__len__()
# print deck_size
print(deck_size)

# create a function to demonstrate selection sort
def selection_sort(cards, deck_size):
    # iterate over range of deck_size
    for i in range(deck_size):
        # assign minimum index to element at cards[i]
        min_index = i
        # iterate over range of i+1 and deck_size
        for j in range(i+1, deck_size):
            # if element at cards[j] is less than element at cards [min_index] then
            if cards[j] < cards[min_index]:
                # assign minimum index to element at cards[j]
                min_index = j
        # swap position of elements
        (cards[i], cards[min_index]) = (cards[min_index], cards[i])
    # return sorted list of cards
    return cards

# print
print("Sorted deck of cards:", selection_sort(cards, deck_size))

