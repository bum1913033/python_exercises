# Create list of numbers
numbers = [1,2,0,4,5,6,7]

# Initialize variables
sum = 0
count = 0
minimum = None
maximum = None

# iterate over elements in list using range
for i in range(len(numbers)):
    sum += numbers[i]
    count += 1

    # assign min max by comparison
    if minimum is None or numbers[i] < minimum:
        minimum = numbers[i]
    
    if maximum is None or numbers[i] > maximum:
        maximum = numbers[i]

# calculate average
average = sum / count

# print
print('sum is', sum)
print('average is', average)
print('count is', count)
print('min is', minimum)
print('max is', maximum)