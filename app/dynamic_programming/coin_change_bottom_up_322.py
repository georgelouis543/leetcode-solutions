from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Bottom Up DP (Tabulation)
        coins.sort()
        dp = [0] * (amount + 1)  # defining the DP Array

        for i in range(1, amount + 1):
            minn = float('inf')

            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break

                minn = min(minn, 1 + dp[diff])

            dp[i] = minn

        if dp[amount] < float('inf'):
            return dp[amount]

        else:
            return -1
