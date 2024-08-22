#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0

    # Create a list to store the minimum coins for each amount up to the total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins needed for a total of 0

    # Build up the dp table
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means total cannot be met by any coins
    return dp[total] if dp[total] != float('inf') else -1


# Example usage:
print(makeChange([1, 2, 25], 37))  # Should print 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Should print -1
