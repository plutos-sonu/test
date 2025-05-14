def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    This function takes a list of numbers (integers or floats) and returns their average.
    If the list is empty, it returns None. The result is rounded to two decimal places.

    Args:
    numbers (list): A list of numbers (int or float)

    Returns:
    float or None: The average of the numbers, rounded to two decimal places.
                   Returns None if the input list is empty.

    Raises:
    TypeError: If the input is not a list or if any element in the list is not a number.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    
    if not numbers:
        return None
    
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numbers")
    
    return round(sum(numbers) / len(numbers), 2)

def multiply(a, b):
    """
    Multiply two numbers.

    This function takes two numbers (integers or floats) and returns their product.

    Args:
    a (int or float): The first number
    b (int or float): The second number

    Returns:
    float: The product of a and b

    Raises:
    TypeError: If either a or b is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")

    return a * b