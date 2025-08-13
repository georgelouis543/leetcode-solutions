def count_elements(nums: list[int]):
    count = 0
    hash_set = set(nums)

    for num in nums:
        if num + 1 in hash_set:
            return True

    return False