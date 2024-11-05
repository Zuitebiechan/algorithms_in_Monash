def counting_sort(a_list) -> list:
    """
    sort a list without comparison

    only efficient when M << N

    Time Complexity:
        - O(N + M + N + M + N) -> O(N+M)

    Aux Space Complexity:
        - if stable: O(M+N) <- count_array
        - if not: O(M)
    """
    # first, find out the maximum item -> O(N * comp), where N is the length of the input list
    max_item = max(a_list)
    
    # second, initialize count_array -> O(M) where M is the maximum item in the input list, also the length of count_array
    count_array = [None] * (max_item+1) # +1 cuz index starts from 1
    for i in range(len(count_array)):
        count_array[i] = [] # [ [],[],[] ... [] ]

    # third, go thru the input list to update the count_array -> O(N)
    for item in a_list:
        count_array[item].append(item) # example: if two 1s, count_array[1] will be [1,1]

    # finally, update the input list -> O(M + N)
    index = 0
    for i in range(len(count_array)): # O(M)
        item = i
        # the length of all sub_arrays is N -> O(N)
        frequency = len(count_array[i])
        for _ in range(frequency):         # reminder: tho nested loops, the time complexity is not square!!!
            a_list[index] = item
            index += 1

    return a_list


### testing
a_list = [6, 3, 1, 7, 2, 8, 1, 7]
print(counting_sort(a_list)) # Expected output: [1, 1, 2, 3, 6, 7, 7, 8]



    