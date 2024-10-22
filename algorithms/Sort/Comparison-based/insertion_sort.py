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
        key = mylist[i] # store the value to compare
        j = i - 1 # get the index before this value
        # if the key value is smaller than the value before it, shift mylist[j] and mylist[j+1] and go j-1
        while j >= 0 and key < mylist[j]:
            mylist[j+1] = mylist[j] # cover the value using the value before it
            j -= 1
        mylist[j+1] = key # finally put the key value at the most front place, now mylist[j+1] is the smallest value in mylist[0...i]