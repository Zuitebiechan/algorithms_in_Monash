def bubble_sort(mylist: list) -> None:
    """
    Sort a list of elements using the bubble sort algorithm.

    Parameters:
    mylist (list): A list of elements to be sorted.

    Time complexity:
    Best case: O(n)
    Worst case: O(n^2), where n is the number of elements in the list 'mylist'.

    Analysis:
    Best case:
    - when the list is already sorted, the inner loop will only loop once.
    Worst case:
    - when the list is sorted in reverse order, the inner loop will loop n-i times for each i.

    Aux Space complexity:
    O(1).

    Correctness:
        Loop invariant:
            - mylist[n-i...n-1] is sorted.
        Termination:
            i will always increment until the end of the list and j will increment until len(mylist)-i-1.

    Stability:
    The bubble sort algorithm is stable. because if the same values, no swapping will happen.
    """
    for i in range(len(mylist)):
        flag = False # check if there is any swap in this iteration
        for j in range(0, len(mylist)-i-1):
            if mylist[j] > mylist[j+1]: # if the current item is larger than the next item, then swap
                # in the end, the largest item will be at the end of mylist
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
                flag = True
        
        if flag is False:
            break
    
    