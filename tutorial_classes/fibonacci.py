# In this case, "arbitrary boundary" refers to the maximum number of elements in the Fibonacci series that the user wants to calculate. 
# The user inputs the boundary number, and the program returns the Fibonacci series up to that number of elements.

def fibonacci(n):
    # Check if the input is less than or equal to 0
    # Return an empty list if so
    if n <= 0:
        return []
    # If the input is 1, return a list with [0]
    elif n == 1:
        return [0]
    # If the input is 2, return a list with [0, 1]
    elif n == 2:
        return [0, 1]
    # For all other inputs
    else:
        # Initialize the list with first two elements [0, 1]
        fib = [0, 1]
        # Loop from 2 to n-1
        for i in range(2, n):
            # Append the sum of the last two elements to the list
            fib.append(fib[-1] + fib[-2])
        # Return the final list
        return fib

# Prompt user for the boundary number
boundary = int(input("Enter the boundary for the Fibonacci series: "))
# Call the fibonacci function and pass the boundary as an argument
# Print the resulting list
print(fibonacci(boundary))
