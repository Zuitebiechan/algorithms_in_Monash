def radix_sort(a_list) -> list:
    """
    To sort a list of integers with very large numbers (M >> N where M is the largest number in the input list and N is the no. of items in the list)

    Time complexity:
        - O(d * N) where d is the digit of the maximum number in the input list and N is the no. of the input list
    
    Aux space complexity:
        - O(N)

    Note:
        if d becomes very large, we can increase base to 100, 1000.... (tradeoff between space and time complexity)
    """
    # first, find the max number in the list -> O(N)
    max_item = a_list[0]
    for item in a_list:
        if item > max_item:
            max_item = item 

    # second, find out the digit of the max number -> O(d) where d is the digit of the maximum number
    d = 0
    while max_item != 0:
        max_item = max_item // 10
        d += 1

    # third, call counting sort d times to sort according to each column -> O(d * N)
    base = 10
    exp = 1
    for _ in range(d):
        a_list = counting_sort_for_radix(a_list, exp, base) # O(N)
        exp *= base
        
    return a_list


def counting_sort_for_radix(arr, exp, base):
    """
    counting sort for radix sort

    Time complexity:
        - O(N)
        - cuz the length of counting_array is 10 which is a constant

    Aux space complexity:
        - O(N) for output list
        - O(10 + N) -> O(N) for count_array
        - so totally O(N) where N is the no. of the array
    """
    n = len(arr)
    output = [0] * n  # store the list after sorting one column digits -> aux space complexity: O(N) where N is the no. of the array

    count_array = [[] for _ in range(base)]

    # first, go thru the array to get the digits and append them to the count_array -> O(N)
    for i in range(n):
        digit = arr[i] // exp % base
        count_array[digit].append(arr[i])

    # second, go thru the count_array left to right to add all numbers to output based on the sequence after sorting the column -> O(N + 10) = O(N)
    index = 0
    for i in range(len(count_array)): 
        frequency = len(count_array[i])
        for j in range(frequency):
            output[index] = count_array[i][j]
            index += 1
    
    return output


a_list = [1, 20, 200, 151, 291, 981, 369, 421, 6711]
print(radix_sort(a_list)) # Expected output: [1, 20, 151, 200, 291, 369, 421, 981, 6711]



