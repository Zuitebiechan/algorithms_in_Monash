# ====================================================== normal one ======================================================
def fibonacci_recursive(n, sum) -> int:
    # basecase 
    if n <= 1:
        return n
    
    # recurrence case
    sum = fibonacci_recursive(n-1, sum) + fibonacci_recursive(n-2, sum)
    return sum

# print(fibonacci_recursive(10, 0))  # 输出：55

# ====================================================== Top-down approach ======================================================
def fibonacci_top_down(n, memo):
    """
    Time Complexity:
        - O(n) due to n times recursive calls

    Aux Space Complexity:
         - O(n) due to recurrence
    """
    if memo[n] != -1:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_top_down(n-1, memo) + fibonacci_top_down(n-2, memo)

    return memo[n]

# n = 10
# memo = [-1] * (n+1)
# print(fibonacci_top_down(n, memo))

# ====================================================== Bottom-up approach ======================================================
def fibonacci_bottom_up(n):
    """
    Time Complexity:
        - O(n) due to go thru the dp array

    Aux Space Complexity:
        - O(n) due to dp array
    """
    if n <= 1:
        return n
    
    dp = [0] * (n+1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# print(fibonacci_bottom_up(n))
