import math


def radix_sort(a_list, base=10) -> list:
    """
    To sort a list of integers with very large numbers (M >> N where M is the largest number in the input list and N is the no. of items in the list)

    Time complexity:
        - O(d * (N+M)) where d is the number of times calling counting-sort
                       N is the no. of the input list and 
                       M is the base (in this case 10)

    Analysis:
        d is the time we call counting-sort; O(N+M) is the time complexity of counting-sort
        Higher base(M) will get lower d
    
    Aux space complexity:
        - O(N)

    Note:
        if d becomes very large, we can increase base to 100, 1000.... (tradeoff between space and time complexity)
    """
    # first, find the max number in the list -> O(N)
    max_item = max(a_list)

    # second, find the number of times calling counting sort under specific base
    num_passes = math.ceil(math.log(max_item+1, base))

    # third, call counting sort num_passes times to sort according to each column -> O(d * N)
    exp = 1
    for _ in range(num_passes):
        a_list = counting_sort_for_radix(a_list, exp, base) # O(N)
        exp *= base
        
    return a_list


def counting_sort_for_radix(arr, exp, base): # O(N) where N is the length of the arr
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
    output = [0] * n  # store the list after sorting one column digits -> aux space complexity: O(N) where N is the length of the array

    count_array = [[] for _ in range(base)]

    # First, go through the array to get the digits and append them to the count_array -> O(N)
    for num in arr:
        digit = (num // exp) % base
        count_array[digit].append(num) # the index of count_array is the rigjtmost digit of this number. i.e. 100, put it into count_array[0]; 231, put it into count_array[1]

    # second, go thru the count_array left to right to add all numbers to output based on the sequence after sorting the column -> O(N + 10) = O(N)
    index = 0
    for bucket in count_array: # O(base) -> O(1)
        for num in bucket:
            output[index] = num
            index += 1

    return output


a_list = [1, 20, 200, 151, 291, 981, 369, 421, 6711]
print(radix_sort(a_list)) # Expected output: [1, 20, 151, 200, 291, 369, 421, 981, 6711]



