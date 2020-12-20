def bubble_sort_help(array: list, fixed: int):

    stop_index = 0

    if fixed == stop_index:
        return array
    
    else:
        a,b = 0, 1
        
        while b != fixed:

            if array[a] > array[b]:
                array[a], array[b] = array[b], array[a]
        
            a += 1
            b += 1
        
        fixed -= 1

        if fixed != 0:
            bubble_sort_help(array, fixed)


def bubble_sort(array: list) -> list:
    """Bubble Sort Algorithm
    Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements
    if they are in wrong order.
    FIRST PASS:
    [5 1 4 2 8] --> [1 5 4 2 8], here algorithm compares the first two elements, and swaps since 5>1.
    [1 5 4 2 8] --> [1 4 5 2 8],Swap since 5 > 4.
    [1 4 5 2 8] --> [1 4 2 5 8],Swap since 5 > 2.
    [1 4 2 5 8] --> [1 4 2 5 8],Now since these elemens are already in order (8 > 5), algorithm does 
    not swap them.
    SECOND PASS
    [1 4 2 5 8] --> [1 4 2 5 8]
    [1 4 2 5 8] ==> [1 2 4 5 8],Swap since 4 > 2.
    [1 2 4 5 8] --> [1 2 4 5 8]
    Now, the array is already sorted, but our algorithm does not know if is completed. The algorithm needs 
    one whole pass without any swap to know it is sorted.
    """

    fixed = len(array)
    array = bubble_sort_help(array, fixed)
    return array

array = [10, 72, 66, 43]  
array = bubble_sort(array)
print(array)
