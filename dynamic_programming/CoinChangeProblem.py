"""
Question Description:
    The coin has different currencies and we want to smallest number of coins to pay.

    Example:
        - currencies: {1,5,10,50}
        - price: 110
        - solution: 50*2 + 10 = 110 -> the smallest number of coins to combine 110 is 3 
"""

def solution(price):
    memo = [-1] * (price+1)

    