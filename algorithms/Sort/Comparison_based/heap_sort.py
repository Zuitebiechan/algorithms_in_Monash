def heapify(arr, n, i):
    largest = i  # 初始化最大元素的位置为 i
    left = 2 * i + 1  # 左子节点的位置
    right = 2 * i + 2  # 右子节点的位置

    # 如果左子节点存在，且左子节点的值大于当前最大值
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 如果右子节点存在，且右子节点的值大于当前最大值
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果最大值不是根节点
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # 交换
        heapify(arr, n, largest)  # 递归地堆化子树

def heap_sort(arr):
    """
    Time Complexity:
        - Best/Worst case: O(nlogn * comp)
    """
    n = len(arr)

    # 构建最大堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 一个接一个地提取元素
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 将当前堆顶（最大值）移到数组末尾
        heapify(arr, i, 0)  # 调整剩下的元素，继续维护堆的性质
    

if __name__ == "__main__":
    arr = [5, 5, 4, 3, 1, 2, 6]
    heap_sort(arr)
    print(arr)
