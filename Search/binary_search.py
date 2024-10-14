def binary_search(arr, target):
    """
    Perform a binary search to find the index of 'target' in a sorted array 'arr'.
    
    Parameters:
    arr (list): A sorted list of elements.
    target: The element to search for in the list.

    Returns:
    int: The index of 'target' in 'arr' if found, otherwise -1 if 'target' is not present.
    """
    # Initialize two pointers representing the start and end of the search space
    left = 0
    right = len(arr) - 1

    # Continue the loop as long as the search space is valid (i.e., left <= right)
    while left <= right:
        # Calculate the middle index to split the array into two halves
        mid = left + (right - left) // 2
        
        # If the target is found at the mid index, return mid
        if arr[mid] == target:
            return mid
        
        # If the target is smaller than the middle element, discard the right half
        elif arr[mid] > target:
            right = mid - 1
        
        # If the target is larger than the middle element, discard the left half
        else:
            left = mid + 1
    
    # If the target is not found, return -1
    return -1

# Example usage:
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7

result = binary_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the array.")