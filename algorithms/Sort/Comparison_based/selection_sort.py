def selection_sort(mylist: list) -> None:
    """
    Sort a list of elements using the selection sort algorithm.

    Parameters:
    mylist (list): A list of elements to be sorted.

    Returns:
    list: A sorted list of elements in ascending order.

    Time complexity:
    O(kn^2), where n is the number of elements in the list 'mylist'. (O(k) is the complexity of comparison)
    Analysis:
    - The outer loop runs n times.
    - The inner loop runs n - i times.
    - The total number of comparisons is n(n - 1) / 2.
    - The total number of swaps is at most n.

    Aux Space complexity:
    O(1).

    Correctness:
        Loop invariant:
            - mylist[0...i-1] is sorted.
            - mylist[0...i-1] ≤ mylist[i...n-1].
        Termination:
            i and j will always increment until the end of the list.

    Stability:
    The selection sort algorithm is not stable.
    Example:
    [4a, 3, 4b, 2] -> [2, 3, 4b, 4a] (4a and 4b are swapped)
    """
    for i in range(len(mylist)):
        min_index = i
        # Find the index of the minimum element in the unsorted part of the list
        for j in range(i+1, len(mylist)):
            if mylist[min_index] > mylist[j]:
                min_index = j

        # Swap the minimum element with the first element of the unsorted part
        mylist[min_index], mylist[i] = mylist[i], mylist[min_index]


if __name__ == "__main__":
    arr = [5, 5, 4, 3, 1, 2, 6]
    selection_sort(arr)
    print(arr)
    