from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = (l + r) // 2

            if mid < len(arr) - 1 and arr[mid + 1] > arr[mid]:
                l = mid + 1

            elif mid > 0 and arr[mid - 1] > arr[mid]:
                r = mid - 1

            else:
                return mid

        return 0
