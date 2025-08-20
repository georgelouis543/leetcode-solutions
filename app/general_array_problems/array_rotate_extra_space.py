nums = [1,2,3,4,5,6,7]
k = 4

n = len(nums)
print(len(nums))
out_list = [0]*len(nums)
print(out_list)

out_list[0: k] = nums[n - k: n + 1]
print(out_list)

out_list[k: n] = nums[0: n - k]

print(out_list)