# create a variable to store string:
message = "What happened was, we reached the moon. But lost in space, I think we got there all too soon.\nAnd in the morning, Sun hits the water. Is this nirvana?"
print(message)
print(message.__len__())

# initialize count variable:
count = 0
letter = 'M'

# for loop to select each letter:
for i in range(message.__len__()):
    if message[i].upper() == letter:
        count += 1

# print count of letter M
print(count)