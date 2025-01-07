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
