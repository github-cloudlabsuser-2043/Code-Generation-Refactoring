def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the input integer n.

    Raises:
    ValueError: If n is a negative integer.

    Examples:
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

choice = int(input("Enter a number to calculate its factorial: "))
if choice < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {choice} is {factorial(choice)}")