class Solution:
    def trailingZeroes(self, n: int) -> int:
        # The number of trailing zeros is the count of factors of 5

        count = 0
        while n >= 5:
            n = n // 5
            count += n

        return count
