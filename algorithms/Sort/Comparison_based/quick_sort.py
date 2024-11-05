
### original one
def quick_sort_out_of_place(arr):
    """
    Description:
        Choosing a pivot and partition the list into two parts, then repeat (recursion) on the two parts.
        After each recursion, the pivot is already on its right position.
        Three ways to partition.

    Time complexity:
        Bestcase:
            - O(N logN) where N is the number of items in the input list
            - cuz the best senario of partition is that we always divide the list into two equal parts, 
              leading to logN height and each height needs O(N) operations
        Worstcase:
            - O(N^2)
            - happens when partition doesn't work (the pivot is always the smallest or largest item of the list)

    Aux space complexity:
            - O(logN)
            - cuz recurrence depth is O(logN)

    Invariants:
        - left <= pivot
        - right > pivot

    Stability:
        - not stable

    Recurrence relation:
        Bestcase:
        - T(1) = b                                          if n = 1;
        - T(N) = c*N + T(N/2) + T(N/2) = c*N + 2T(N/2)      if n > 1;
        Worstcase:
        - T(1) = b                                          if n = 1;
        - T(N) = C*N + T(N-1)                               if n > 1;
    
    Average Time Complexity Analysis:
        Let h be the recurrence depth. The cost of each recurrence level is O(N) cuz we need to do partition (go thru the list).
        Therefore the total cost is O(h*N).

        On average senario, each recurrence level we divide the list into two parts: larger part (3N/4) and smaller part (N/4),
        and the base case is when the list has only one item.
        Therefore, N * (3N/4)^h = 1 -> h = log_4/3(N) -> total cost: O(log_4/3(N) * N) = O(N logN)

    """
    ### Out-of-place (need temporary memory to store items)
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]       # left is an array containing all elements that are smaller than the pivot
    middle = [x for x in arr if x == pivot]    # middle is an array containing all elements that are equal to the pivot
    right = [x for x in arr if x > pivot]      # right is also an array containing all elements that are greater than the pivot
    return quick_sort_out_of_place(left) + middle + quick_sort_out_of_place(right)

### Inplace
## Hoare's
''' Python implementation of QuickSort using Hoare's 
partition scheme. '''

''' This function takes first element as pivot, and places
      all the elements smaller than the pivot on the left side
      and all the elements greater than the pivot on
      the right side. It returns the index of the last element
      on the smaller side '''

def partition_hoare(arr, low, high):
    """
    unstable
    """
    pivot = arr[low]  # Choose the first element as the pivot
    i = low - 1
    j = high + 1

    while True:
        # Move i to the right until an element >= pivot is found
        i += 1
        while arr[i] < pivot:
            i += 1

        # Move j to the left until an element <= pivot is found
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # If pointers have crossed, return j
        if i >= j:
            return j

        # Swap arr[i] and arr[j]
        arr[i], arr[j] = arr[j], arr[i]


''' The main function that implements QuickSort 
arr --> Array to be sorted, 
low --> Starting index, 
high --> Ending index '''

def quickSort_Hoares(arr, low, high):
    ''' pi is partitioning index, arr[p] is now 
    at right place '''
    if (low < high):

        pi = partition_hoare(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort_Hoares(arr, low, pi)
        quickSort_Hoares(arr, pi + 1, high)


## Lomuto's
''' Python implementation of QuickSort using Lomuto's 
partition scheme. '''

''' This function takes last element as pivot, and places
      all the elements smaller than the pivot on the left side
      and all the elements greater than the pivot on
      the right side. It returns the index of the last element
      on the smaller side '''
def lomuto_partition(arr, low, high):
    """
    Invariant:
        - each time after the loop, i+1 is the index of the first item in the arr that is greater than the pivot
        - each time after the loop, arr[0 ... i] <= pivot
    Backwards:
        - when arr is large, many swap operations would occur
    """
    pivot = arr[high]  # 选择最后一个元素作为基准
    i = low - 1  # 指针i初始化为low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # 交换arr[i]和arr[j]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # 将基准放置在正确位置
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = lomuto_partition(arr, low, high)
        quick_sort(arr, low, pi - 1)  # 递归排序左子数组
        quick_sort(arr, pi + 1, high)  # 递归排序右子数组

## Dutch National Flag
def dutch_national_flag_partition(arr, low, high):
    """
    三指针分区方法， 每次把list分为 < pivot, = pivot, > pivot 三个部分

    Invariant:
        after each loop:
        - arr[0 ... boundary1] < pivot
        - arr[boundary1 ... i] = pivot
        - arr[i ... boundary2] unprocessed yet
        - arr[boundary2 ... n] > pivot
    """
    pivot = arr[low]
    boundary1 = low
    boundary2 = high
    i = low + 1

    while i <= boundary2:
        if arr[i] < pivot:
            arr[i], arr[boundary1] = arr[boundary1], arr[i]
            boundary1 += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[boundary2] = arr[boundary2], arr[i]
            boundary2 -= 1
        else:
            i += 1
    
    return boundary1, boundary2

def quick_sort_dutch_national_flag(arr, low, high):
    """
    QuickSort using DNF partition.
    """
    if low < high:
        boundary1, boundary2 = dutch_national_flag_partition(arr, low, high)
        quick_sort_dutch_national_flag(arr, low, boundary1 - 1)
        quick_sort_dutch_national_flag(arr, boundary2 + 1, high)



''' Function to print an array '''
def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()

# test
arr = [7, 3, 8, 4, 7]
n = len(arr)
quickSort_Hoares(arr, 0, n - 1)
print("Sorted array:")
printArray(arr, n)


