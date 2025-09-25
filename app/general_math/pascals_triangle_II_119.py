from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        if rowIndex == 0:
            return res

        for i in range(1, rowIndex + 1):
            prev_row = res[i - 1]
            curr_row = [1]

            for j in range(1, i):
                curr_row.append(prev_row[j - 1] + prev_row[j])

            curr_row.append(1)
            res.append(curr_row)

        return res[rowIndex]
