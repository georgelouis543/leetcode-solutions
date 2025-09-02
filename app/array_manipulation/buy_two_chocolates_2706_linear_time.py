from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min_value_1 = float('inf')
        min_value_2 = float('inf')

        for p in prices:
            min_value_1 = min(p, min_value_1)

        skipped = False
        for p in prices:
            if p == min_value_1 and not skipped:
                skipped = True
                continue

            min_value_2 = min(p, min_value_2)

        print(min_value_1)
        print(min_value_2)

        if min_value_1 + min_value_2 <= money:
            return money - min_value_1 - min_value_2

        return money