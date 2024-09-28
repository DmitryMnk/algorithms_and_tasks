from typing import List


def max_profit(prices: List[int]) -> int:
    min_price = float('inf')
    max_prof = 0

    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_prof:
            max_prof = profit
    return max_prof

print(
    max_profit([7,6,4,3,1])
)