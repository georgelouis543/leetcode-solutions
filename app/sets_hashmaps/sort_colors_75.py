from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color_map = {"red": 0, "white": 0, "blue": 0}

        for num in nums:
            if num == 0:
                color_map["red"] += 1
            if num == 1:
                color_map["white"] += 1
            if num == 2:
                color_map["blue"] += 1

        print(color_map)

        i = 0
        for color in color_map:
            if color == "red" and color_map[color] > 0:
                for _ in range(0, color_map[color]):
                    nums[i] = 0
                    i += 1
            elif color == "white" and color_map[color] > 0:
                for _ in range(0, color_map[color]):
                    nums[i] = 1
                    i += 1
            elif color == "blue" and color_map[color] > 0:
                for _ in range(0, color_map[color]):
                    nums[i] = 2
                    i += 1

