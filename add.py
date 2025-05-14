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