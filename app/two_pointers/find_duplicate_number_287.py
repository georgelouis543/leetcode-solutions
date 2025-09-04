from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Use floyd's cycle finding algorithm
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        print(slow)

        # Find the entrance of the cycle
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow