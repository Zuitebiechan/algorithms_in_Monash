from quick_sort import quick_sort_dutch_national_flag


def partition(arr, pivot):
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
    less, equal, greater = partition(arr, median_of_medians) # O(N)

    # 根据第 k 小的元素在三部分中的位置进行判断
    if k < len(less):
        return quick_select(less, k)  # 如果第 k 小的元素在 less 中，递归查找
    elif k < len(less) + len(equal):
        return median_of_medians  # 如果第 k 小的元素在等于 pivot 的部分，直接返回 pivot
    else:
        return quick_select(greater, k - len(less) - len(equal))  # 如果第 k 小的元素在 greater 中，递归查找


# 示例用法
arr = [12, 3, 5, 7, 4, 19, 26, 21, 18]
k = 4  # 找到第 4 小的元素
print(f"The {k}th smallest element is: {quick_select(arr, k)}")