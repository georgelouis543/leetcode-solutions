from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        out_list = []
        arr.sort()
        print(arr)

        min_diff = float('inf')

        j = 1
        for i in range(0, len(arr) - 1):
            curr_diff = abs(arr[j] - arr[i])
            min_diff = min(curr_diff, min_diff)
            j += 1

        print(min_diff)
        print(arr)

        k = 1
        for i in range(0, len(arr) - 1):
            if abs(arr[k] - arr[i]) == min_diff:
                out_list.append([arr[i], arr[k]])

            k += 1

        print(out_list)

        return out_list