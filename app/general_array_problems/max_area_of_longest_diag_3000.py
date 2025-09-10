from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = float('-inf')
        max_area = float('-inf')

        for dim in dimensions:
            diag_length = dim[0] ** 2 + dim[1] ** 2
            curr_area = dim[0] * dim[1]

            if diag_length > max_diagonal:
                max_diagonal = diag_length
                max_area = curr_area

            elif diag_length == max_diagonal:
                max_area = max(curr_area, max_area)

        return max_area

