def zeroSumSubarray(nums):
    # Write your code here.
    seen_sums = {0}
    curr_sum = 0

    for num in nums:
        curr_sum = curr_sum + num
        if curr_sum in seen_sums:
            return True
        else:
            seen_sums.add(curr_sum)

    print(seen_sums)
    return False
