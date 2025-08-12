def binary_search(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            r = mid - 1
        elif target > nums[mid]:
            l = mid + 1

    return -1


print(binary_search([1,3,4,5,6,7,8], 6))
