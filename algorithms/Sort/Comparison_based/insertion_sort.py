def insertion_sort(mylist: list) -> None:
    """
    Sort a list of elements using the insertion sort algorithm.

    Parameters:
    mylist (list): A list of elements to be sorted.

    Returns:
    list: A sorted list of elements in ascending order.

    Time complexity:
    Best case: O(n)
    Worst case: O(n^2), where n is the number of elements in the list 'mylist'.

    Analysis:
    Best case:
    - when the list is already sorted, the inner loop will not execute.
    Worst case:
    - when the list is sorted in reverse order, the inner loop will execute i times for each i.

    Aux Space complexity:
    O(1).

    Correctness:
        Loop invariant:
            - mylist[0...i-1] is sorted.
        Termination:
            i will always increment until the end of the list and j will decrement until reach -1.

    Stability:
    The insertion sort algorithm is stable <- if the same values, no shifting will happen.
    """
    for i in range(1, len(mylist)):
        key = mylist[i]  # Store the value to be inserted
        j = i - 1
        
        # Shift elements of mylist[0...i-1], that are greater than key, to one position ahead
        # of their current position to make space for key
        while j >= 0 and mylist[j] > key:
            mylist[j + 1] = mylist[j]
            j -= 1

        # Insert the key at its correct position
        mylist[j + 1] = key

if __name__ == "__main__":
    arr = [5, 5, 4, 3, 1, 2, 6]
    insertion_sort(arr)
    print(arr)