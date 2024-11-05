from quick_sort import quick_sort_dutch_national_flag

# ====================================================== QuickSelect using MoM ======================================================

def partition_mom(arr, pivot):
    """
    分区函数：根据基准 pivot 将数组分为三部分：小于 pivot、等于 pivot 和大于 pivot。
    """
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return less, equal, greater

def quick_select(arr, k):
    """
    使用 Median of Medians 算法来选择数组中第 k 小的元素。

    Time Complexity:
        - O(n)
    """
    # Basecase: if the length of arr is less than 5, no need to use MoM, just use any sort algorithm (except counting sort) to sort it and get the k-th element 
    if len(arr) <= 5:
        quick_sort_dutch_national_flag(arr, 0, len(arr)-1)
        return arr[k]

    # Recurrence case: if the length of arr is more than 5, use MoM to get the list of medians and then call quick_select again
    medians = []
    for i in range(0, len(arr), 5):
        group = arr[i:i + 5]
        quick_sort_dutch_national_flag(group, 0, len(group)-1) # O(N/5) -> O(N)
        medians.append(group[len(group) // 2])  # 找到每组的中位数

    # 递归地找到中位数的中位数
    median_of_medians = quick_select(medians, len(medians) // 2)

    # 以 median_of_medians 为基准对数组进行分区
    less, equal, greater = partition_mom(arr, median_of_medians) # O(N)

    # 根据第 k 小的元素在三部分中的位置进行判断
    if k < len(less):
        return quick_select(less, k)  # 如果第 k 小的元素在 less 中，递归查找
    elif k < len(less) + len(equal):
        return median_of_medians  # 如果第 k 小的元素在等于 pivot 的部分，直接返回 pivot
    else:
        return quick_select(greater, k - len(less) - len(equal))  # 如果第 k 小的元素在 greater 中，递归查找

# # 示例用法
# arr = [12, 3, 5, 7, 4, 19, 26, 21, 18]
# k = 4  # 找到第 4 小的元素
# print(f"The {k}th smallest element is: {quick_select(arr, k)}")



# ====================================================== Normal QuickSelect ======================================================

def partition(arr, l, r) -> int:
    """
    Partition funtion for QuickSelect. 
    It will return the index the pivot and patition the array into two parts which are left to the pivot and right to the pivot

    :param: 
        * arr: an array to partition
        * l: the left end of the array
        * r: the right end of the array

    :return: the index the pivot
    """

    # choose the last item as pivot
    pivot = arr[r]

    # initialize pointer i to 0, it will always points to the first item in the array that is greater than the pivot; after the loop, it will be the index of the pivot
    i = l

    # go thru the array from l to r
    for j in range(l, r):
        if arr[j] <= pivot:
            # put items less than the pivot to front
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]

    return i

def quick_select(arr, k: int, l, r) -> int:
    """
    QuickSelect algorithm to find out the k-th smallest item in an array.
    The index of the k-th smallest item will be k-1.

    :param: 
        * arr: a list of integers 
        * k: an integer number representing the k-th smallest number to find

    :return: The k-th smallest number in the array

    Time Complexity:
        - Basecase: O(N) where N is the length of the array,
                         happens when the pivot we choose at the first time is the k-th smallest number so that we only go thru the array one time
        
        - Average: O(N). This is because after one partition we know that our target item is either on the left part or right part. Therefore we only
                         need to recursively partition one part (* core difference from QuickSort -> O(nlogn)), so the length of the array we need to go thru will be like
                         n + n/2 + n/4 + ... + 1 < 2n -> O(N)

        - Worstcase: O(N^2). Each time the pivot we choose is the smallest or largest item in the array which leads to extremely unbalanced partition.
                             Therefore the length of the array will be like n + n-1 + n-2 + ... + 1 -> O(N^2)

    Aux Space Complexity:
        - O(NlogN) for recursion
    """
    index = partition(arr, l, r)

    # we found the correct number, return
    if index == k-1:
        return arr[index]
    # the target is in the right part
    elif index < k-1:
        return quick_select(arr, k, index+1, r)
    # the target is in the left part
    else:
        return quick_select(arr, k, l, index-1)

def test_quick_select():
    # Test case 1: Basic case
    arr = [3, 2, 1, 5, 4]
    k = 3
    assert quick_select(arr, k, 0, len(arr) - 1) == 3, f"Failed on Test case 1, got {quick_select(arr, k, 0, len(arr) - 1)}"

    # Test case 2: Array with duplicates
    arr = [7, 10, 4, 3, 20, 15]
    k = 4
    assert quick_select(arr, k, 0, len(arr) - 1) == 10, f"Failed on Test case 2, got {quick_select(arr, k, 0, len(arr) - 1)}"

    # Test case 3: Array with negative and positive numbers
    arr = [7, -2, 3, 5, -1, 4, 6, 8]
    k = 5
    assert quick_select(arr, k, 0, len(arr) - 1) == 5, f"Failed on Test case 3, got {quick_select(arr, k, 0, len(arr) - 1)}"

    # Test case 4: Array with all elements the same
    arr = [1, 1, 1, 1, 1]
    k = 3
    assert quick_select(arr, k, 0, len(arr) - 1) == 1, f"Failed on Test case 4, got {quick_select(arr, k, 0, len(arr) - 1)}"

    # Test case 5: Array is already sorted
    arr = [1, 2, 3, 4, 5]
    k = 2
    assert quick_select(arr, k, 0, len(arr) - 1) == 2, f"Failed on Test case 5, got {quick_select(arr, k, 0, len(arr) - 1)}"

    print("All test cases passed!")

# Run the test
test_quick_select()
