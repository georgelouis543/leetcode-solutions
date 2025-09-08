from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        summ = n
        i = 1

        while i <= n - 1:
            j = summ - i
            if "0" not in str(i) and "0" not in str(j):
                return [i, j]

            i += 1

        return [0, 0]
