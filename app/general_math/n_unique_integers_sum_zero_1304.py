from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        # Sum of n natural numbers = n(n + 1) / 2
        # Sum of n - 1 natural numbers = n(n - 1) / 2
        # 1 + 2 + 3 + ... + (n - 1) = n(n - 1) / 2
        # -n(n - 1)/2 + 1 + 2 + ... + (n - 1) = 0
        # n(1 - n)/2 + 1 + 2 + 3 + ... + (n - 1) = 0
        # Result list would be [n(1 - n)//2, 1, 2, 3, ..., (n - 1)]

        res = [i for i in range(0, n)]
        res[0] = (n * (1 - n)) // 2
        return res
