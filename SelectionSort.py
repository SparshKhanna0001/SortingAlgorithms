def selection_sort(array: list) -> list:
    """Selection Sort Algorithm
    
    The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering 
    ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two 
    subarrays in a given array.

    1) The subarray which is already sorted.
    2) Remaining subarray which is unsorted.

    In every iteration of selection sort, the minimum element (considering ascending order) from the 
    unsorted subarray is picked and moved to the sorted subarray.

    Following example explains the above steps:

    arr[] = 64 25 12 22 11

    Find the minimum element in arr[0...4] and place it at beginning
    11 25 12 22 64

    Find the minimum element in arr[1...4] and place it at beginning of arr[1...4]
    11 12 25 22 64

    Find the minimum element in arr[2...4] and place it at beginning of arr[2...4]
    11 12 22 25 64

    Find the minimum element in arr[3...4] and place it at beginning of arr[3...4]
    11 12 22 25 64 
    
    """

    array1 = []

    while True:
        
        min = array[0]
        for j in array:
            if j < min:
                min = j
        array1.append(min)
        array.remove(min)

        if len(array) == 0:
            break

    del array
    array = array1.copy()
    del array1
    del min    
    return array
