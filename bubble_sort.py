def bad_bubble_sort(l: list, reverse: bool = False) -> list:
    """
    Sorts a list using an inefficient bubble sort algorithm.

    The function attempts to sort the list in ascending or descending order 
    based on the `reverse` flag. The function compares each element with the 
    previous one and swaps them if they are out of order. If a swap occurs, 
    the pointer (starting at 1) resets to 1, causing the comparison process 
    to restart from the beginning. 

    Parameters:
    - l (list): List to be sorted.
    - reverse (bool): If True, sort in descending order, otherwise ascending. Default is False.

    Returns:
    - list: Sorted list.

    Raises:
    - Exception: If `reverse` is not a boolean.
    - Exception: If `l` is not a list.

    Example:
    >>> bad_bubble_sort([3, 1, 5, 4, 2], reverse=False)
    [1, 2, 3, 4, 5]
    
    >>> bad_bubble_sort([3, 1, 5, 4, 2], reverse=True)
    [5, 4, 3, 2, 1]
    """
    
    pointer = 1

    if not isinstance(reverse, bool):
        raise Exception("reverse must be True or False")
    
    if not isinstance(l, list):
        raise Exception("This function takes a list")

    if not reverse:
        while pointer < len(l):
            if l[pointer] > l[pointer-1]:
                pointer+=1
            else:
                l[pointer], l[pointer-1] = l[pointer-1], l[pointer]
                pointer=1
    
    if reverse:
        while pointer < len(l):
            if l[pointer] < l[pointer-1]:
                pointer+=1
            else:
                l[pointer-1], l[pointer] = l[pointer], l[pointer-1]
                pointer=1

    
    return l

def bubble_sort(l: list, reverse: bool=False) -> list:
    """
    Sorts a list using the bubble sort algorithm.

    Args:
        l (list): The list to be sorted.
        reverse (bool, optional): If True, sorts the list in descending order. 
                                  If False (default), sorts in ascending order.

    Returns:
        list: The sorted list.

    Raises:
        Exception: If the 'reverse' argument is not a boolean.
        Exception: If 'l' is not a list.

    Example:
        >>> bubble_sort([3, 1, 4, 1, 5, 9], reverse=False)
        [1, 1, 3, 4, 5, 9]

        >>> bubble_sort([3, 1, 4, 1, 5, 9], reverse=True)
        [9, 5, 4, 3, 1, 1]
    """

    if not isinstance(reverse, bool):
        raise Exception("reverse must be True or False")

    if not isinstance(l, list):
        raise Exception("This function takes a list")
    
    for i in range(len(l)):
        swapped = False
        for j in range(1, len(l)-i):
            if not reverse:
                if l[j] < l[j-1]:
                    l[j], l[j-1] = l[j-1], l[j]
                    swapped = True


            else:
                if l[j] > l[j-1]:
                    l[j-1], l[j] = l[j], l[j-1]
                    swapped = True
                    
        if not swapped:
            break
        
    return l
